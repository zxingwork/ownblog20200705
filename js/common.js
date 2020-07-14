function register(){
    const user = $('#user').val();
    const password = $('#password').val();
    const senddata = {
        "username": user,
        "password": password
    }
    const ipaddr = document.location.hostname;
    const url = "http://"+ipaddr+":9527/register";
    console.log(url);

    $.ajax({
        type: "post",
        url: url,
        contentType: "application/json;charset=utf-8",
        datatype: "json",
        async: false,
        data: JSON.stringify(senddata),
        success: function (data){
            for (var key in data){
                console.log(data[key]);
            }
            alert(data)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown){
            alert("请求在连接过程中出错误..\n" + errorThrown);
        }
    });

}