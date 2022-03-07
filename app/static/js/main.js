const search = document.getElementsByClassName('search_input')[0];

search.addEventListener('keyup', async event => {
    let keyword = event.target.value.trim();
    if (!keyword) {
        keyword = "%"
    }
    const response = await (await fetch(`http://127.0.0.1:8000/store?keyword=${keyword}`)).json();
    console.log(keyword)
    const suggestions_pannel = document.querySelector(".suggestions_pannel");
    suggestions_pannel.innerHTML = '';
    response.forEach(function (suggested) {
        let div = document.createElement('div');
        div.setAttribute('class', 'shop_detail02')

        let title = document.createElement('strong');
        let info = document.createElement('div');
        let address = document.createElement('span');
        title.innerHTML = suggested.name;
        address.innerHTML = suggested.address

        div.appendChild(title);
        info.appendChild(address);
        div.appendChild(info);

        suggestions_pannel.appendChild(div);
        // 클릭처리 
        div.onclick = () => {
            document.getElementsByName('iframe1')[0].style.display = "None";
            document.querySelector(".background").className = "background show";
            const contents = document.getElementsByClassName('contents')[0];
            if (suggested.result) {
                contents.innerHTML = `
                <strong>혜택 확인</strong>
                <hr class="connectHeaderRule"></hr>
                <p>
                    설문조사를 완료해 주셔서 감사합니다. 
                    BURGER KING®은 귀하를 다시 저희 식당을 방문하도록 초대하고자 합니다. 
                    다음 방문 시 티켓에 표시한 주문을 제시하는 것을 잊지 마십시오. 
                    티켓에 다음 코드를 기재해야 합니다.
                </p>
                <strong class="valcode">확인 코드: ${suggested.result}</strong>
                <p>참여해 주셔서 감사합니다.</p>
                `;
            } else {
                contents.innerHTML = `
                <strong class="valcode">BURGER KING® 고객 만족도 설문조사에 참여해 주셔서 감사합니다.</strong>
                <p>귀하의 솔직한 의견을 소중하게 생각하며, 시간을 내어 설문조사에 참여해 주신 데 대해 감사를 드립니다.</p>
                <p>설문조사를 마치시면 초대장에 입력할 수 있는 인증 코드를 제공해 드립니다.</p>
                <p>Please enter the survey code located on the front of your receipt.</p>
                <form method="post" action="http://127.0.0.1:8000/update/${suggested.name}" id="frm" target="iframe1">
                    <label for="CN1" class="sr-only">CN1</label>
                    <input class="coupon-length-3 " type="text" autocomplete="off" id="CN1" name="CN1" aria-label="CN1" maxlength="3"
                    onKeyup="inputMoveNumber(this);">
                    -
                    <label for="CN2" class="sr-only">CN2</label>
                    <input class="coupon-length-3 " type="text" autocomplete="off" id="CN2" name="CN2" aria-label="CN2" maxlength="3"
                    onKeyup="inputMoveNumber(this);">
                    -
                    <label for="CN3" class="sr-only">CN3</label>
                    <input class="coupon-length-3 " type="text" autocomplete="off" id="CN3" name="CN3" aria-label="CN3" maxlength="3" 
                    onKeyup="inputMoveNumber(this);">
                    -
                    <label for="CN4" class="sr-only">CN4</label>
                    <input class="coupon-length-3 " type="text" autocomplete="off" id="CN4" name="CN4" aria-label="CN4" maxlength="3"
                    onKeyup="inputMoveNumber(this);">
                    - 
                    <label for="CN5" class="sr-only">CN5</label>
                    <input class="coupon-length-3 " type="text" autocomplete="off" id="CN5" name="CN5" aria-label="CN5" maxlength="3" 
                    onKeyup="inputMoveNumber(this);">
                    - 
                    <label for="CN6" class="sr-only">CN6</label>
                    <input class="coupon-length-1 " type="text" autocomplete="off" id="CN6" name="CN6" aria-label="CN6" maxlength="1"
                    onKeyup="inputMoveNumber(this);">
                </form>
                <div>
                    <input type="button" id="NextButton" name="NextButton" value="시작" class="NextButton" onclick="change(); document.getElementById('frm').submit();">
                </div>
                `;
            }
        }
        if (!keyword) {
            suggestions_pannel.innerHTML = '';
        }
    });
});

function change() {
    document.getElementsByName('iframe1')[0].style.display = "block";
}
function close() {
    document.querySelector(".background").className = "background";
}

function inputMoveNumber(num) {
    if (isFinite(num.value) == false) {
        alert("카드번호는 숫자만 입력할 수 있습니다.");
        num.value = "";
        return false;
    }
    max = num.getAttribute("maxlength");
    if (num.value.length >= max) {
        num.nextElementSibling.focus();
    }
}

window.onload = function () {
    search.dispatchEvent(new KeyboardEvent('keyup', { 'key': 'Enter' }));
};

document.querySelector("#close").addEventListener("click", close);

