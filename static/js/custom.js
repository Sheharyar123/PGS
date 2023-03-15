$(document).ready(function () {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  $("#contact-form").on("submit", function (e) {
    e.preventDefault();
    const name = document.querySelector("#id_name").value;
    const email = document.querySelector("#id_email").value;
    const subject = document.querySelector("#id_subject").value;
    const message = document.querySelector("#id_message").value;
    const csrftoken = getCookie("csrftoken");
    console.log(name);
    $.ajax({
      type: "POST",
      url: "/",
      data: {
        name: name,
        email: email,
        subject: subject,
        message: message,
        csrfmiddlewaretoken: csrftoken,
      },

      success: function (response) {
        if (response.status == "success") {
          swal({
            title: "Your message was sent successfully!",
            icon: "success",
          });
        } else {
          swal({
            title: "There was a problem sending your message!",
            icon: "error",
          });
        }
        $("#contact-form")[0].reset();
      },
    });
  });
});
