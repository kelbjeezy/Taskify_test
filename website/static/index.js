function showAndHideImage() {
    var image = document.getElementById('myImage');
    var image2 = document.getElementById('myImage2');
    var image3 = document.getElementById('myImage3');
    var image4 = document.getElementById('myImage4');
    var image5 = document.getElementById('myImage5');
    image.style.opacity = '1';
    image2.style.opacity = '1';
    image3.style.opacity = '1';
    image4.style.opacity = '1';
    image5.style.opacity = '1';
    
    image.style.visibility = 'visible';
    image2.style.visibility = 'visible';
    image3.style.visibility = 'visible';
    image4.style.visibility = 'visible';
    image5.style.visibility = 'visible';

  
    setTimeout(function() {
      image.style.opacity = '0';
      image2.style.opacity = '0';
      image3.style.opacity = '0';
      image4.style.opacity = '0';
      image5.style.opacity = '0';

    }, 1500); // 2 seconds for image display
  
    setTimeout(function() {
      image.style.display = 'none';
      image2.style.display = 'none';
      image3.style.display = 'none';
      image4.style.display = 'none';
      image5.style.display = 'none';
      
      image.style.visibility = 'hidden';
      image2.style.visibility = 'hidden';
      image3.style.visibility = 'hidden';
      image4.style.visibility = 'hidden';
      image5.style.visibility = 'hidden';

      window.location.href="/task_page"; //Changing the href so that pepe doesn't keep staying on the screen after even refreshing
    }, 2000); // 3 seconds for fade-out transition and hiding the image
  }
  
// Check if the query parameter "showImage" is present
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.has('task-deleted')) {
    showAndHideImage(); // Call the function to show and hide the image
}

function deleteTask(taskId){
    fetch('/delete-task', {
        method: 'POST',
        body: JSON.stringify({ taskId: taskId })
    }).then((_res) => {
        window.location.href = "/task_page?task-deleted=true";
        showAndHideImage();
    })
}

function completeTask(taskId){
    fetch('/complete-task', {
        method: 'POST',
        body: JSON.stringify({ taskId: taskId })
    }).then((_res) => {
        window.location.href = "/task_page";
    })
}

function uncompleteTask(taskId){
    fetch('/uncomplete-task', {
        method: 'POST',
        body: JSON.stringify({ taskId: taskId })
    }).then((_res) => {
        window.location.href = "/task_page";
    })
}

