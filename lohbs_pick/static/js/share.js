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
