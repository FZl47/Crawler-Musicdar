// Send Ajax
function send_ajax(Url, Data = {}, Method = 'POST', Success, Failed, convert_json = true) {
    let This = this

    if (Success == undefined) {
        Success = function (response) {
        }
    }
    if (Failed == undefined) {
        Failed = function (response) {
        }
    }

    $.ajax({
        url: Url,
        data: convert_json ? JSON.stringify(Data) : Data,
        type: Method,
        processData: false,
        contentType: false,
        headers: {
            'X-CSRFToken': window.CSRF_TOKEN
        },
        success: function (response) {
            Success(response)
        },
        failed: function (response) {
            Failed(response)
        },
        error: function (response) {
            Failed(response)
            notify({
                title: 'ارور',
                message: 'ارتباط با سرور برقرار نشد',
                closeOnClick: true,
                positionClass: 'nfc-top-right',
                showDuration: 8500,
                theme: 'error'
            })
        }
    })
}

function random_string(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
        counter += 1;
    }
    return result;
}

function createNotify(options) {
    // delete old notify elements
    document.querySelectorAll('.ncf-container').forEach((e) => {
        e.remove()
    })
    let id = `notify-${random_string(10)}`
    let notify_el = document.createElement('div')
    notify_el.id = `${id}`
    notify_el.className = `ncf-container ${options.positionClass}`
    notify_el.innerHTML = `
        <div class="ncf ${options.theme}"><p class="ncf-title">${options.title}</p><p class="nfc-message">${options.message}</p></div>
    `
    document.body.append(notify_el)
    let element = document.getElementById(id)
    if (options.closeOnClick) {
        element.addEventListener('click', function () {
            element.remove()
        })
    }
    let show_duration_timeout = null
    try {
        clearTimeout(show_duration_timeout)
    } catch (e) {
    }
    show_duration_timeout = setTimeout(function () {
        element.remove()
    }, options.showDuration,)
}


function createLoading(element, options) {
    let loading = document.createElement('div')
    loading.className = `loading-element loading-circle-${options.size}`
    let color = options.color || '#1ee696'
    loading.style = `
        border-top-color:${color};
        border-right-color:${color};
    `
    let loading_blur = document.createElement('div')
    loading_blur.className = 'loading-blur-element'
    element.append(loading_blur)
    element.append(loading)
    element.classList.add('loading-element-parent')
    element.setAttribute('disabled', 'disabled')
}

function removeLoading(element) {
    element.querySelector('.loading-element').remove()
    element.querySelector('.loading-blur-element').remove()
    element.classList.remove('loading-element-parent')
    element.removeAttribute('disabled')
}


function getParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
            tmp = item.split("=");
            if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}


let err_message_notify = getParameter('error')
if (err_message_notify) {
    createNotify({
        title: 'ارور',
        message: err_message_notify,
        closeOnClick: true,
        positionClass: 'nfc-top-right',
        showDuration: 8500,
        theme: 'error'
    })
}
let success_message_notify = getParameter('success')
if (success_message_notify) {
    createNotify({
        title: 'موفق',
        message: success_message_notify,
        closeOnClick: true,
        positionClass: 'nfc-top-right',
        showDuration: 8500,
        theme: 'success'
    })
}