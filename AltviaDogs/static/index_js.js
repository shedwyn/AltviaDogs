// js specific to index Page
'use strict';
//

function retrieveDateChoiceValue(){
  return $("#date_choice").val();
}

function checkForValue(dateChoice){
  if (dateChoice === "") {
    return false;
  } else {
      return true;
  };
}

function checkForValidDate(dateChoice){
  var regexLayout = /^(\d{4})(\-)(\d{2})(\-)(\d{2})$/;
  if (dateChoice.match(regexLayout)) {
    return true;
  } else {
    return false;
  };
}


function checkForCorrectDateFormat(dateChoice){
  if (checkForValue(dateChoice) === false) {
    return false;
  } else if (checkForValidDate(dateChoice)=== false) {
    return false;
  } else {
    return true;
  };
}

//

function formatDateForPost(dateChoice){
  var newDate = dateChoice.split('-');
  var dateAsInts = [];
  for (var i in newDate) {
    dateAsInts.push(Number(newDate[i]))
  };
  return dateAsInts
}

//

function rejectWithMessage(){
  alert("whoops, that wasn't right.  Try again.")
}

// main functions

function correctDateEntry(dateChoice){
  if (checkForValidDate(dateChoice) === false){
    return false;
  } else {
      formatDateForPost(dateChoice);
      return true;
  }
}

//activation and registration


function registerGlobalEventHandlers() {
  // const sourceForm = document.getElementByID('date-choice-form');
  // const dateChoice = document.getElementByID('date_choice').value;
  console.log('00 - Nothing to see here, folks');
  // .on - I want it to eval just before submitting and return to the same
  // state as when person hit "submit" if there was an error, and have an
  // error alert, but keep the data in the fields as/is
  $('#date-choice-form').on('submit', function(event){
    event.preventDefault();
    var dateChoiceValue = retrieveDateChoiceValue();
    if (checkForCorrectDateFormat(dateChoiceValue) === true) {
      var newDate = formatDateForPost(dateChoiceValue);
      return newDate;
    } else {
      console.log('1b - found Incorrect Date Format in ' + dateChoiceValue);
      rejectWithMessage();
    }
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
