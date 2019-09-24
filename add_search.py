import requests

def main():
    # 入力
    zipcode = input('郵便番号を入力>')
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
    # 計算
    response = requests.get(url)
    res_list = response.json()['results'][0]

    # 出力
    address = f'{res_list["address1"]} {res_list["address2"]} {res_list["address3"]}'
    print(address)


if __name__ == '__main__':
    main()