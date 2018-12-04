
//获取指定case_id的用例信息
var CaseInit = function (case_id) {

    function getCaseInfo() {
        // 获取某个用例的信息
        $.post("/interface/get_case_info/", {
            "caseId": case_id,
        }, function (resp) {
            if (resp.success === "true"){
                console.log("状态", resp.success);
                let result = resp.data;
                console.log("结果", result);
                document.getElementById("req_name").value = result.name;
                document.getElementById("req_url").value = result.url;
                document.getElementById("req_header").value = result.reqHeader;
                document.getElementById("req_parameter").value = result.reqParameter;
                document.getElementById("assert_text").value = result.assertText;

                if (result.req_method === "post"){
                    document.getElementById("post").setAttribute("checked", "");
                }

                if (result.req_type === "json"){
                    document.getElementById("json").setAttribute("checked", "");
                }

                // 初始化菜单 -->待完善
                ProjectInit('project_name', 'module_name', result.projectName, result.moduleName)
            }else {
                //console.log("状态", resp.success);
                window.alert("用例id不存在");
            }

        });
    }
    //调用getCaseInfo函数
    getCaseInfo();
}


// 获取用例列表
let CaseListInit = function () {

    let options = ""
    function getCaseListInfo() {
        //获取某个用例的信息
        $.get("/interface/get_case_list", {}, function (resp) {
            if (resp.success === "true"){
                console.log(resp.data);
                let cases = resp.data;
                for (let i = 0; i < cases.length; i++){
                    let option = '<input type="checkbox" name="' + cases[i].name
                        + '" value="' + cases[i].id + '" /> ' + cases[i].name + '<br>'

                    options = options + option;
                }
                let devCaseList = document.querySelector(".caseList");
                devCaseList.innerHTML = options;

            }else {
                window.alert(resp.message);
            }
            }
        );
    }
    // 调用getCaseListInfo函数
    getCaseListInfo();
}



