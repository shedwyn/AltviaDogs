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
  console.log(dateChoice + 'Time to split');
  var newDate = dateChoice.split('-');
  console.log('Here is the new date ' + newDate);
  var dateAsInts = [];
  for (var i in newDate) {
    dateAsInts.push(Number(newDate[i]))
  };
  console.log('Date As Integer List '+ dateAsInts)
  return dateAsInts
}

//

function rejectWithMessage(){
  console.log('Got as Far as running Reject With Message')
  alert("whoops, that wasn't right.  Try again.")
}

// main functions

function correctDateEntry(dateChoice){
  if (checkForValidDate(dateChoice) === false){
    console.log('invalid date');
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
    console.log('begin process of checking format');
    if (checkForCorrectDateFormat(dateChoiceValue) === true) {
      console.log('1a - found Correct Date Format in ' + dateChoiceValue);
      var newDate = formatDateForPost(dateChoiceValue);
      return true;
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
