// js specific to index Page
'use strict';
//

function retrieveDateChoiceValue(){
  return $("#date_choice").val()
}

function checkForValue(dateChoice){
  if (dateChoice === "") {
    return false
  } else {
      return true
  };
}

function checkForCorrectDateFormat(dateChoice){
  console.log(dateChoice)
  var regexLayout = /^(\d{4})(\-)(\d{2})(\-)(\d{2})$/;
  if (checkForValue(dateChoice) === false && !(dateChoice.match(regexLayout))){
    rejectWithMessage
    return false
  } else {
    return true
  };
}

function checkForValidDate(dateChoice){
  if (checkForValue(dateChoice)===false){

    rejectWithMessage
  } else {

  };
}

//

function formatDateForPost(dateChoice){
  console.log("DateForPost")
}

//

function rejectWithMessage(){
  alert("whoops, that wasn't right.  Try again.")
}

// main functions

function correctDateEntry(dateChoice){
  if (checkForValidDate(dateChoice) === false){
    console.log('invalid date')
    rejectWithMessage
  } else {
      formatDateForPost(dateChoice)
      return true
  }
}

//activation and registration


function registerGlobalEventHandlers() {
  // const sourceForm = document.getElementByID('date-choice-form');
  // const dateChoice = document.getElementByID('date_choice').value;
  console.log("starting");
  // .on - I want it to eval just before submitting and return to the same
  // state as when person hit "submit" if there was an error, and have an
  // error alert, but keep the data in the fields as/is
  $("#date-choice-form").on("change", function(){
    let dateChoice = retrieveDateChoiceValue;
    checkForCorrectDateFormat(dateChoice);
    console.log("date was checked");
  });
  //$(#date-choice-form).on("submit", function(){
  //  let dateChoice = retrieveDateChoiceValue;
  //  checkForCorrectDateFormat(dateChoice);
  //  formatDateForPost(dateChoice);
  //  

  //})
    //event.preventDefault();
  };

registerGlobalEventHandlers()
