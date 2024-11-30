// Wait for the document to be ready before executing any JavaScript
document.addEventListener("DOMContentLoaded", function () {
  // Example: Simple form validation for the service request creation
  const requestForm = document.querySelector("#service-request-form");
  if (requestForm) {
    requestForm.addEventListener("submit", function (event) {
      const requestType = document.querySelector("#id_request_type").value;
      const details = document.querySelector("#id_details").value;

      // Check if request type and details are filled
      if (!requestType || !details) {
        alert("Please fill out all required fields.");
        event.preventDefault(); // Prevent form submission
      }
    });
  }

  // Example: Hide or show the status section based on service request status
  const statusElements = document.querySelectorAll(".status-toggle");
  statusElements.forEach(function (element) {
    element.addEventListener("click", function () {
      const statusDetails = element.nextElementSibling;
      if (
        statusDetails.style.display === "none" ||
        statusDetails.style.display === ""
      ) {
        statusDetails.style.display = "block";
      } else {
        statusDetails.style.display = "none";
      }
    });
  });

  // Additional interactive features can go here...
});
