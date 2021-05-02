function atLeastOneCheckbox(myClass) {
  const boxes = Array.from(document.querySelectorAll(myClass));
  return boxes.reduce((acc, curr) => acc || curr.checked, false);
}

function numberTechniques() {
  $("select[name='techniques']").each(function (index) {
    $(this).attr("name", "techniques" + index);
  });
}