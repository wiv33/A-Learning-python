import datetime
import os
import sys
import time

import pandas as pd
from selenium.webdriver import Keys

from BrowserModule import Browser


def send_approval(account_info, receivers, 수신=[], 공람=[], 감사=[], 참조=[]):
    print("sender : ", account_info)
    _id, _pw, _url, sender_nick_name = account_info
    b = Browser(view_mode=True)
    d = b.d
    try:

        print(f"\t\tstart {_id}, {_pw}, {sender_nick_name}, to receivers : {receivers}")
        d.get(_url + "/home")

        login(_id, _pw, b)

        # 결재 tab 버튼
        b.click_wait_selector(
            "#main-wrapper > header > page-header > div > page-global-navi-bar > a.workflow-btn.ng-scope > span.name")

        time.sleep(3)
        child_num = 2
        b.click_wait_selector(
            "#main-wrapper > section > workflow-vue-component > section > div > div > a > button > span:nth-child(2)")
        b.click_wait_selector(
            f"#main-wrapper > section > workflow-vue-component > section > section > div > div.document-select-layout__content > div.document-select-layout__content_right > div:nth-child(2) > div > div:nth-child({child_num}) > div > div.category__document > div > div")

        time.sleep(2)
        print("handles", d.switch_to.window(d.window_handles[1]))

        b.click_wait_selector(
            "body > div.approval-popup-layout > div > div.document-detail-view__header.detail-view-header > div > div.approval-process-button__edit > button > span")

        ## loop 요소
        # 결재라인 유저 추가
        receiver_nick_names = []
        for idx in range(len(receivers)):
            _temp_name = receivers.iloc[idx].nick_name
            if _temp_name == '딸기':
                break
            receiver_nick_names.append(_temp_name)

        for _nick_name in receiver_nick_names[::-1]:
            # 결재라인 추가 버튼 클릭
            b.click_wait_selector(
                "#d-modal-container > div > section > div > section > div > div.department-member.list-container > div.select-area > div.content-wrapper > div > div > table > tbody > tr > tr > td.approval-line-edit-form__line-column-8 > div > div.plus-button > button")

            # 결재 라인 이름 입력
            line_target = b.wait_selector(
                "#d-modal-container > div > section > div > section > div > div.department-member.list-container > div.select-area > div.content-wrapper > div > div > table > tbody > tr > tr:nth-child(2) > td.approval-line-edit-form__line-column-5 > div > div > div > div > div > div > input[type=text]")
            line_target.send_keys(_nick_name)
            b.click_wait_selector("body > ul > li")



        # 수신이 있으면 추가, 추후에 메일 수신했는지 체크
        for nick_name_key in 수신:
            _temp_name = receiver_info.loc[receiver_info['nick_name'] == nick_name_key].nick_name
            recept_element = b.wait_selector(
                "#d-modal-container > div > section > div > section > div > div.department-member.list-container > div:nth-child(3) > div > div.content-wrapper__tag-input-contents > div > div > div > div > input[type=text]")
            recept_element.send_keys(_temp_name)
            b.click_wait_selector("body > ul > li")

        # 공람
        for nick_name_key in 공람:
            _temp_name = receiver_info.loc[receiver_info['nick_name'] == nick_name_key].nick_name
            recept_element = b.wait_selector(
                "#d-modal-container > div > section > div > section > div > div.department-member.list-container > div:nth-child(7) > div > div.content-wrapper__tag-input-contents > div > div > div > div > input[type=text]")
            recept_element.send_keys(_temp_name)
            b.click_wait_selector("body > ul > li")

        # 감사

        # 참조

        # 적용
        b.click_wait_selector("#d-modal-container > div > section > div > footer > button.eZWsHA.m.primary")

        ## loop end

        # 제목 입력
        _from_to = f"{sender_nick_name} to {','.join(receiver_nick_names)} " \
                   f"with 수신: {','.join(수신)}" \
                   f"with 공람: {','.join(공람)} " \
                   f" at {datetime.datetime.now()} "
        b.wait_selector(
            "body > div.approval-popup-layout > div > div.document-detail-view__body.detail-view-body > div.approval-edit-body-info > div.approval-edit-body-info__drag-area > div.edit-body-title > div > div.edit-body-title__contents > input").send_keys(
            _from_to)

        # 기안하기 버튼 -> 확인 -> 확인
        b.click_wait_selector(
            "body > div.approval-popup-layout > div > div.document-detail-view__header.detail-view-header > div > div.approval-process-button__draft > button > span")
        b.click_wait_selector("#d-modal-container > div > section > div > footer > button.eZWsHA.m.primary")
        b.click_wait_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span")

        # 보낸 메일 검증 폴더 생성
        os.mkdir(f"{_from_to}")
        # d.close()
        time.sleep(2)
        d.save_screenshot(f'{_from_to}/0_send_list_{sender}.png')
        return receiver_nick_names, _from_to

    except Exception as _e:
        print(_e)
        d.quit()
    finally:
        d.quit()


def login(_id, _pw, b):
    b.wait_selector(
        "#content > div > form > fieldset > div.input-wrap > div:nth-child(1) > div > span > input[type=text]").send_keys(
        _id)
    b.wait_selector(
        "#content > div > form > fieldset > div.input-wrap > div:nth-child(2) > div > span > input[type=password]").send_keys(
        _pw)
    b.click_wait_selector("#content > div > form > fieldset > div.button-area > button")

    time.sleep(3)
    try:
        unlock(b)
    except Exception as _e:
        print(_e)
    print("\t\tcomplete login", _id)
    time.sleep(3)


def unlock(b):
    try:
        b.click_wait_selector(
            "body > div.modal.ng-isolate-scope.setting-modal.dooray-setting-content.renewal-preview-modal.in > div > div > div.renewal-preview-modal-footer.ng-scope > button",
            wait_time=7)
    except Exception as e:
        print("unlock error ", e)
        pass


def check_receipt(receiver_list, mail_title, recept_df, 수신=[], 공람=[]):
    target_list = receiver_list + 수신 + 공람
    recept_cnt = len(target_list)
    print("receipt list", target_list)
    for x, nick_name_key in enumerate(target_list):
        _id, _pw, _url, _nick_name = recept_df.loc[recept_df['nick_name'] == nick_name_key].iloc[0].values
        print("recept range", _id, _url)
        b = Browser(view_mode=True)
        d = b.d
        d.get(_url + "/home")

        time.sleep(2)

        login(_id, _pw, b)

        # mail_title = "번개 to 얼쑤,벼리,러버,자두,연두 at 2023-01-19 18:16:30.643979"
        # mail click
        b.click_wait_selector(
            "#main-wrapper > header > page-header > div > page-global-navi-bar > a.mail-btn.ng-scope > span.name")
        print(f"mail title: {mail_title}")
        for element in b.wait_selector_all("#main-wrapper span.subject.ellipsis.ng-binding.ng-scope"):
            if not element:
                continue
            print(element.text and element.text.__contains__(mail_title))
            if element.text and element.text.__contains__(mail_title):
                element.click()
                time.sleep(2)
                d.save_screenshot(f"./{mail_title}/{x}_{_nick_name}.png")

                print("결재 라인 텍스트: ", element.text)
                if (_nick_name in 수신 or _nick_name in 공람) and element.text.__contains__("문서 알림"):
                    recept_cnt -= 1
                    break

                _approval_btn = b.wait_selector(
                    "#mailContentsView-subject-anchor > section > div.dooray-contents.default-html4css > div > div > div > table > tbody > tr > td > table > tbody > tr:nth-child(8) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(1) > a",
                    wait_time=7)
                d.execute_script("arguments[0].click();", _approval_btn)
                d.switch_to.window(d.window_handles[1])
                b.click_wait_selector(
                    "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary",
                    wait_time=7)
                b.click_wait_selector("body > div.el-message-box__wrapper > div > div.el-message-box__btns > button")

                time.sleep(1)
                recept_cnt -= 1
                break

    if recept_cnt != 0:
        raise Exception(f"{recept_cnt}, 메일 수신 확인 불가: {mail_title}")


def check_sender_final_recept(_sender_info_df, mail_title):
    _id, _pw, _url, sender_nick_name = _sender_info_df
    b = Browser(view_mode=True)
    d = b.d

    d.get(_url + "/home")
    login(_id, _pw, b)

    b.click_wait_selector(
        "#main-wrapper > header > page-header > div > page-global-navi-bar > a.mail-btn.ng-scope > span.name")
    for element in b.wait_selector_all("#main-wrapper span.subject.ellipsis.ng-binding.ng-scope"):
        if not element:
            continue
        print("완료 문서 확인: ", element.text)
        if element.text and element.text.startswith("[완료]") and element.text.__contains__(mail_title):
            element.click()
            time.sleep(2)
            d.save_screenshot(f"./{mail_title}/final_recept_{sender_nick_name}.png")
            return

    raise Exception(f"완료 결재 확인 불가: {_id}")


def external_ids(l):
    result = list(receiver_info.loc[receiver_info['nick_name'].isin(l)]['nick_name'].values)
    print("external result :", result)
    return result


if __name__ == '__main__':
    sender = "qwer3" if len(sys.argv) < 2 else sys.argv[0]
    receiver = "ulssu" if len(sys.argv) < 2 else sys.argv[2:]
    account_df = pd.read_csv("account-beta.csv", index_col='_idx')
    sender_info = account_df.loc[sender]
    receiver_info = account_df.loc[account_df.index != sender].iloc[:, :]
    print("sender info: ", sender_info.to_list())

    수신_list = external_ids(['연두'])

    공람_list = external_ids(['자두'])

    sent_names, mail_title = send_approval(sender_info.to_list(), receiver_info, 수신=수신_list, 공람=공람_list)
    check_receipt(sent_names, mail_title, receiver_info, 수신_list)
    check_sender_final_recept(sender_info, mail_title)
