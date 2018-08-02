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
  $("#date-choice-form").on("change", function(){
    const dateChoice = retrieveDateChoiceValue;
    console.log(checkForCorrectDateFormat(dateChoice));
    console.log("date was checked")
  });
    //event.preventDefault();
  };

registerGlobalEventHandlers()
