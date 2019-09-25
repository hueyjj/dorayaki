export function getCookie(name: string): string {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log("Cookie value: " + cookieValue);
    return cookieValue as string;
}

export const fetchThreads = () => {
  fetch("http://localhost:8000/api/v1/threads/", {
    method: "GET",
    headers: {
      Accept: "application/json",
    }
  })
    .then(resp => resp.json())
    .then(data => {
      console.log(data);
    });
}

export const getCsrfToken = () => {
  fetch("http://localhost:8000/poop/", {
    credentials: "include",
  })
  .then(resp => resp.text())
  .then(data => {
    console.log(data);
  });
}

const loginFormData = new FormData();
loginFormData.append("username", "foo@gmail.com")
loginFormData.append("password", "bar")

export const login = () => {
  fetch("http://localhost:8000/auth/login/", {
    method: "POST",
    credentials: "include",
    headers: {
      "Accept": "*/*",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: loginFormData,
    // body: JSON.stringify({
    //   "username": "foo@gmail.com",
    //   "password": "bar",
    // }),
  })
    .then(resp => resp.text())
    .then(data => {
      console.log(data);
    });
}