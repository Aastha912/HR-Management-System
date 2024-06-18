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

  function showAllRows() {
    var hiddenRows = document.querySelectorAll('#employee-table tbody tr.hidden');
    hiddenRows.forEach(function(row) {
        row.classList.remove('hidden');
    });
    // Hide the "Show All" link after it's clicked
    document.querySelector('a').style.display = 'none';
}
  