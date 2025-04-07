document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btn_translate').addEventListener('click', function() {
        const languageCode = document.getElementById('language_code').value;
        
        if (languageCode) {
            fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('hello').textContent = data.hello;
                })
                .catch(error => console.error('Error:', error));
        }
    });
}); 