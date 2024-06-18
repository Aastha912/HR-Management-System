// To-do list functionality
const addButton = document.getElementById("add-button");
const newTaskInput = document.getElementById("new-task");
const taskList = document.getElementById("task-list");

addButton.addEventListener("click", function() {
    const newTask = newTaskInput.value;
    if (newTask) {
      const listItem = document.createElement("li");
      listItem.textContent = newTask;
  
      // Create both complete and delete buttons
      const completeButton = document.createElement("button");
      completeButton.textContent = "Complete";
      completeButton.addEventListener("click", function() {
        this.parentNode.classList.add("completed");
      });
  
      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Delete";
      deleteButton.addEventListener("click", function() {
        this.parentNode.remove(); // Remove the entire list item
      });
  
      // Append both buttons to the list item
      listItem.appendChild(completeButton);
      listItem.appendChild(deleteButton);
  
      taskList.appendChild(listItem);
      newTaskInput.value = "";
    }
  });


  document.addEventListener("DOMContentLoaded", function() {
    // Function to fetch calendar data from the server
    function fetchCalendarData(monthIndex, year) {
        // This function is not needed if you're only displaying the current month
    }

    // Set the current month name in the calendar
    const currentMonthElement = document.querySelector('.monthly_calendar h3');
    const currentMonthName = new Date().toLocaleString('en-US', { month: 'long' });
    currentMonthElement.textContent = currentMonthName;
});

// Function to update the system time
function updateSystemTime() {
  const now = new Date();
  let hours = now.getHours();
  const amPM = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12 || 12; // Convert 24-hour time to 12-hour time
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  const systemTime = `${hours}:${minutes}:${seconds} ${amPM}`;
  
  // Update the input field with the system time
  document.getElementById('systemTime').value = systemTime;
}

// Update system time initially and then every second
updateSystemTime();
setInterval(updateSystemTime, 1000);


const form = document.querySelector("form"),
fileInput = document.querySelector(".file-input"),
progressArea = document.querySelector(".progress-area"),
uploadedArea = document.querySelector(".uploaded-area");

// form click event
form.addEventListener("click", () =>{
  fileInput.click();
});

fileInput.onchange = ({target})=>{
  let file = target.files[0]; //getting file [0] this means if user has selected multiple files then get first one only
  if(file){
    let fileName = file.name; //getting file name
    if(fileName.length >= 12){ //if file name length is greater than 12 then split it and add ...
      let splitName = fileName.split('.');
      fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
    }
    uploadFile(fileName); //calling uploadFile with passing file name as an argument
  }
}

// file upload function
function uploadFile(name){
  let xhr = new XMLHttpRequest(); //creating new xhr object (AJAX)
  xhr.open("POST", "php/upload.php"); //sending post request to the specified URL
  xhr.upload.addEventListener("progress", ({loaded, total}) =>{ //file uploading progress event
    let fileLoaded = Math.floor((loaded / total) * 100);  //getting percentage of loaded file size
    let fileTotal = Math.floor(total / 1000); //gettting total file size in KB from bytes
    let fileSize;
    // if file size is less than 1024 then add only KB else convert this KB into MB
    (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024*1024)).toFixed(2) + " MB";
    let progressHTML = `<li class="row">
                          <div class="content">
                            <div class="details">
                              <span class="name">${name} • Uploading</span>
                              <span class="percent">${fileLoaded}%</span>
                            </div>
                            <div class="progress-bar">
                              <div class="progress" style="width: ${fileLoaded}%"></div>
                            </div>
                          </div>
                        </li>`;
    // uploadedArea.innerHTML = ""; //uncomment this line if you don't want to show upload history
    uploadedArea.classList.add("onprogress");
    progressArea.innerHTML = progressHTML;
    if(loaded == total){
      progressArea.innerHTML = "";
      let uploadedHTML = `<li class="row">
                            <div class="content upload">
                              <div class="details">
                                <span class="name">${name} • Uploaded</span>
                                <span class="size">${fileSize}</span>
                              </div>
                            </div>
                          </li>`;
      uploadedArea.classList.remove("onprogress");
      // uploadedArea.innerHTML = uploadedHTML; //uncomment this line if you don't want to show upload history
      uploadedArea.insertAdjacentHTML("afterbegin", uploadedHTML); //remove this line if you don't want to show upload history
    }
  });
  let data = new FormData(form); //FormData is an object to easily send form data
  xhr.send(data); //sending form data
}




