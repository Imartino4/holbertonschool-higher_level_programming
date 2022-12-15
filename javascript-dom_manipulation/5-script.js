
const upid = document.getElementById('update_header');
upid.addEventListener('click', updateHeader);

function updateHeader() {
    document.querySelector("header").innerHTML = `New Header!!!`
    };