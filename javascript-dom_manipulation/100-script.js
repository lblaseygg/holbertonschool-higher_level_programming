document.addEventListener('DOMContentLoaded', function() {
    const list = document.querySelector('.my_list');

    // Add item functionality
    document.getElementById('add_item').addEventListener('click', function() {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        list.appendChild(newItem);
    });

    // Remove last item functionality
    document.getElementById('remove_item').addEventListener('click', function() {
        const items = list.getElementsByTagName('li');
        if (items.length > 0) {
            list.removeChild(items[items.length - 1]);
        }
    });

    // Clear list functionality
    document.getElementById('clear_list').addEventListener('click', function() {
        list.innerHTML = '';
    });
}); 