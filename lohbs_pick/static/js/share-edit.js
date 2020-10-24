var fileUrl =  document.getElementById("imageInputLabel").innerHTML;
(function deleteParentDir(){
    var dirArray = fileUrl.split('/');
    console.log(dirArray);
    document.getElementById("imageInputLabel").innerHTML = dirArray[dirArray.length - 1];
})()
