// js specific to index Page
'use strict';
//inputs

function checkForValue(aValue){
  if (aValue !== "") {
    return true
  }
  else {
    return false
  }
}

function checkForValidDate(aValue){
  if (checkForBlankValue(aValue)===false){
    return false
  }
  if (checkCorrectDateFormat(aValue)===false){
    return false
  }
  else {
    return true
  }
}

//transform

function formatDateForPost(aValue){

}

//create

function rejectWithMessage(){
  alert("whoops, that wasn't right.  Try again.")
}

//mains


function correctDateEntry(aValue){
  if (checkForValidDate(aValue) === false){
    rejectWithMessage
  }
  else {
    formatDateForPost(aValue)
  }
}

//registration


document.getElementById('date-choice-form').addEventListener('submit', function(){
  let dateChoice = document.getElementById('date_choice').value
  correctDateEntry(dateChoice)
})
