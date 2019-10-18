function setReadonly(){
        let idc="#{{ case.id }} input";
        alert(idc);
        $(idc).attr("readonly", false);
        $(idc).attr("type", "text");
      }

      $(function () {
        let idc="#{{ case.id }}-edit";
        $(idc).click(setReadonly);
      });

      function addTr(trObj) {
          let tr="<tr id=\"{{ case.id }}\">\n" +
              "            <td>\n" +
              "              <div class=\"layui-unselect layui-form-checkbox\" lay-skin=\"primary\" data-id='2'><i class=\"layui-icon\">&#xe605;</i></div>\n" +
              "            </td>\n" +
              "            <td>{{ case.id }}<input style=\"width: 25px\" type=\"hidden\" id=\"cid\" value=\"{{ case.id }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.uid }}<input style=\"width: 80px\" type=\"hidden\" id=\"uid\" value=\"{{ case.uid }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.module }}<input style=\"width: 60px\" type=\"hidden\" id=\"module\" value=\"{{ case.module }}\" readonly=\"readonly\" ></td>\n" +
              "            <td>{{ case.case_name2 }}<input style=\"width: 250px\" type=\"hidden\" id=\"case_name2\" value=\"{{ case.case_name2 }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.para1 }}<input style=\"width: 25px\" type=\"hidden\" id=\"para1\" value=\"{{ case.para1 }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.para2 }}<input style=\"width: 25px\" type=\"hidden\" id=\"para2\" value=\"{{ case.para2 }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.para3 }}<input style=\"width: 25px\" type=\"hidden\" id=\"para3\" value=\"{{ case.para3 }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.createby }}<input style=\"width: 25px\" type=\"hidden\" id=\"createby\" value=\"{{ case.createby }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.c_time }}<input style=\"width: 25px\" type=\"hidden\" id=\"c_time\" value=\"{{ case.c_time }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.upt_time }}<input style=\"width: 25px\" type=\"hidden\" id=\"upt_time\" value=\"{{ case.upt_time }}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.sort}}<input style=\"width: 25px\" type=\"hidden\" id=\"sort\" value=\"{{ case.sort}}\" readonly=\"readonly\"></td>\n" +
              "            <td>{{ case.run }}<input style=\"width: 25px\" type=\"hidden\" id=\"run\" value=\"{{ case.run }}\" readonly=\"readonly\"></td>\n" +
              "            </tr>\n";
          $(#trObj).after(tr);
      }
