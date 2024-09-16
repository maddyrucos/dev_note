let forms = document.querySelectorAll('.note-form');
forms.forEach( form => {
    form.addEventListener('change', function(event) {
        let formData = new FormData(this);
        let note_id = this.getAttribute('note-id');
        fetch(note_id+'/edit', {
                method: 'POST',
                body: formData
            }
        )
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.log('Error: ' + error);
        })
    });
})