/**
 * Created by alex on 11/24/16.
 */


//run this script before submit,to make sure all chosen options all selected
function CheckSelectedOptions() {
    $("select[data-type='m2m_chosen'] option").prop("selected",true);
    RemoveDisabledAttrs();
}


function RemoveDisabledAttrs() {
    $("input").removeAttr("disabled");
    $("select").removeAttr("disabled");
}



function  PostAndAddAnother() {
    console.log($("form"))
}