const unameInput = document.getElementById('uname');
const upassInput = document.getElementById('upass');
const usernameError = document.getElementById('username-error');
const passwordError = document.getElementById('password-error');
const submitButton = document.querySelector('loginbtn');

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