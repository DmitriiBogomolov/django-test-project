

function register(){

  let button = document.querySelector('.form-button');
  button.disabled = true;
  button.classList.add("disabled");

  let formData = $('.form').serialize();

    $.ajax({
      type: "POST",
      url: "/register/",
      data: formData,
      dataType: "text",
      cache: false,
      success: (data) => {
        if (data=='ok'){
          alert('User has been created.');
          window.location.href = "/"
        }
        else {
          let errors = JSON.parse(data);
          updateErrorList(errors);
          button.disabled = false;
          button.classList.remove("disabled");
        }
      }
    });
    return false;
}

function updateErrorList(errors){
  let errorList = document.querySelector('.error-list');
  errorList.innerHTML = "";

  for(errorArray in errors){
    errors[errorArray].forEach( (error) => {
      errorList.innerHTML += "<li>"+error+"</li>";
    });
  }
}
