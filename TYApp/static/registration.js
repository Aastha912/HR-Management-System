const unameInput = document.getElementById('uname');
const upassInput = document.getElementById('upass');
const upass1Input = document.getElementById('upass1');
const usernameError = document.getElementById('username-error');
const passwordError = document.getElementById('password-error');
const confirmPasswordError = document.getElementById('confirm-password-error');
const submitButton = document.querySelector('registerbtn');

// Validate username on input
unameInput.addEventListener('input', function(event) {
  const uname = event.target.value;

  if (uname.length > 6) {
    usernameError.textContent = 'Username must be 6 Alphabets or less.';
    submitButton.disabled = true;
  } else if (username.trim() === '') {
    usernameError.textContent = 'Username cannot be empty.';
    submitButton.disabled = true;
  } else {
    usernameError.textContent = '';
    submitButton.disabled = false; // Enable submit if both username and password are valid
  }
});

// Validate password on input
upassInput.addEventListener('input', function(event) {
  const upass = event.target.value;

  if (upass.length < 8) {
    passwordError.textContent = 'Password must be at least 8 characters long.';
    submitButton.disabled = true;
  } else if (password.trim() === '') {
    passwordError.textContent = 'Password cannot be empty.';
    submitButton.disabled = true;
  } else {
    passwordError.textContent = '';
    submitButton.disabled = false; // Enable submit if both username and password are valid
  }
});
// Validate confirmation password on input
upass1Input.addEventListener('input', function (event) {
    const confirmation = event.target.value;
  
    if (confirmation !== upass1Input.value) {
      confirmPasswordError.textContent = 'Passwords must match.';
      submitButton.disabled = true;
    } else {
      confirmPasswordError.textContent = '';
      submitButton.disabled = !(validatePassword() && validateConfirmation()); // Only enable submit if both password and confirmation are valid
    }
  });
  
  // Function to validate password complexity (replace with your desired requirements)
  function validatePassword() {
    const password = upassInput.value;
    // Ensure password meets complexity requirements (e.g., minimum length, mix of uppercase/lowercase, numbers, symbols)
    return true; // Replace with actual validation logic
  }
  
  // Function to check if password and confirmation match
  function validateConfirmation() {
    return upassInput.value === upass1Input.value;
  }