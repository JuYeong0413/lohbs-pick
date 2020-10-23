// share new & edit
function filePreview(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();
        let fileType = input.files[0].type;
        let imageElement = document.getElementById('show-image-tag')

        reader.onload = function (e) {
            e.preventDefault()

            if (fileType.includes('image') === true) {
                if (imageElement !== null) { imageElement.remove(); }

                let newImage = document.createElement('img'); 
                $(newImage).attr('id', 'show-image-tag');
                $(newImage).attr('src', e.target.result);
                $(newImage).css('width', '50%');
                
                $('#file-content').append(newImage);
                $('#file-content').addClass('mb-3');
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

// share main page
function readMore() {
  var dots = document.getElementById('dots');
  var moreText = document.getElementById('more');
  var btnText = document.getElementById('readMoreBtn');

  if (dots.style.display === 'none') {
    dots.style.display = 'inline';
    btnText.innerHTML = 'Read More  <i class="fa fa-angle-right">';
    moreText.style.display = "none";
  } else {
    dots.style.display = 'none';
    btnText.innerHTML = 'Read less';
    moreText.style.display = 'inline';
  }
}
