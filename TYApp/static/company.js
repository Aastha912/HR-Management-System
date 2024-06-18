document.addEventListener("DOMContentLoaded", function() {
    // Function to generate and display dates for the current month
    function generateCalendarDates() {
        const currentDate = new Date();
        const currentMonthElement = document.getElementById('currentMonth');
        const currentMonthName = currentDate.toLocaleString('en-US', { month: 'long' });
        currentMonthElement.textContent = currentMonthName;

        const daysInMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0).getDate();
        const datesContainer = document.getElementById('calendarDates');
        datesContainer.innerHTML = '';

        let dateIndex = 1;
        for (let weekIndex = 0; weekIndex < 5; weekIndex++) { // Assuming 5 weeks for simplicity
            const row = document.createElement('tr');
            for (let dayIndex = 0; dayIndex < 7; dayIndex++) {
                const cell = document.createElement('td');
                if (dateIndex <= daysInMonth) {
                    cell.textContent = dateIndex;
                    dateIndex++;
                }
                row.appendChild(cell);
            }
            datesContainer.appendChild(row);
        }
    }

    // Call the function to generate and display dates for the current month
    generateCalendarDates();
});

function showAnnouncementForm() {
    var form = document.querySelector('.announcement-form');
    form.style.display = 'block'; // Display the form
  }
  
  
  $(document).ready(function() {
    $("#announcement-form").submit(function(event) {
        event.preventDefault(); // Prevent default form submission
  
        // Validate the form before submitting (optional, but recommended for user experience)
        if (validateForm()) {
  
            // Collect form data using FormData to handle file uploads
            let formData = new FormData(this);
  
            // Use AJAX to submit the form data to the server
            $.ajax({
                url: $(this).attr('action'), // Get the form's action URL
                type: 'POST',
                data: formData,
                contentType: false, // Set to false for FormData
                processData: false, // Set to false for FormData
                success: function(response) {
                    // Handle successful submission (e.g., redirect, display success message)
                    console.log("Announcement created successfully!");
  
                    // Optionally, clear the form and show a success message
                    $("#announcement-form")[0].reset(); // Reset the form
                    $("#announcement-form").append("<p class='success-message'>Announcement created successfully!</p>");
  
                    // Remove the success message after a few seconds (optional)
                    setTimeout(function() {
                        $(".success-message").remove();
                    }, 3000); // Remove after 3 seconds
                },
                error: function(error) {
                    // Handle error (e.g., display error message to the user)
                    console.error("Error submitting form:", error);
                    $("#announcement-form").append("<p class='error-message'>An error occurred while creating the announcement. Please try again later.</p>");
  
                    // Remove the error message after a few seconds (optional)
                    setTimeout(function() {
                        $(".error-message").remove();
                    }, 3000); // Remove after 3 seconds
                }
            });
        }
    });
  });

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


document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('btn').addEventListener('click', function (event) {
      event.preventDefault();
      var form = document.getElementById('form-id');
      form.submit();
  });

  document.getElementById('login-button').addEventListener('click', function () {
      document.getElementById('login-box').classList.remove('login-box-hidden');
  });

  document.getElementById('close-button').addEventListener('click', function () {
      document.getElementById('login-box').classList.add('login-box-hidden');
  });
});
document.querySelectorAll('.toggle-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    var detailsRow = this.closest('tr').nextElementSibling;
    if (detailsRow.style.display === 'none' || detailsRow.style.display === '') {
      detailsRow.style.display = 'table-row';
    } else {
      detailsRow.style.display = 'none';
    }
  });
});


