function closeAlert(event) {
  var alertBox = event.target.closest(".bg-blue-100"); // Find the closest alert box
  alertBox.style.display = "none"; // Hide the alert box
}
