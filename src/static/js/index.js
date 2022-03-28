let openInfo = (evt, tabInfo) => {
  let i, tabcontent, tablinks

  tabcontent = document.getElementsByClassName('tabcontent')
  for (i=0; i<tabcontent.length; i++) {
    tabcontent[i].style.display = 'none'
  }

  tablinks = document.getElementsByClassName('tablinks')
  for (i=0; i<tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(' active', '')
  }

  document.getElementById(tabInfo).style.display = 'block'
  evt.currentTarget.className += ' active'
}

document.getElementById("defaultOpen").click()

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})
