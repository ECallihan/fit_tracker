function atLeastOneCheckbox(myClass){
  const boxes = Array.from(document.querySelectorAll(myClass));
  return boxes.reduce((acc, curr) => acc || curr.checked, false);
}