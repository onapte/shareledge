document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#id_content').className = "form-control";
    document.querySelector('#sbmt').onclick = function() {
        var data = CKEDITOR.instances.djv.getData();
        document.querySelector('#id_content').value = data;
    };
    
});