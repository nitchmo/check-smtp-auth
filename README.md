# SMTP-AUTHの確認スクリプト

メールサーバーの構築やメンテナンスを担当していると「念の為、SMTP-AUTHが効いているか確認しときたい。」って事があります。  
しかし、over SSL/TLSな環境では結構確認が大変。  

ところが Pythonのsmtplibライブラリを使うと簡単にチェックできちゃいました。

## 使い方・・・と言うか出力例

host, port, user, pwdの変数を設定して、
`python check-smtp-auth.py`を実行してください。

```log
# 正常に認証が通った場合の出力例
Connected  smtp.hostname.tld : 587
> EHLO: [ 250 ]
smtp.hostname.tld
STARTTLS
(以下略...)

> STARTTLS: [ 220 ]
2.0.0 Ready to start TLS
> LOGIN: [ 235 ]
2.7.0 Authentication successful
```

```log
# パスワードが間違ってた場合の出力例
Connected  smtp.hostname.tld : 587
> EHLO: [ 250 ]
smtp.hostname.tld
STARTTLS
(以下略...)

> STARTTLS: [ 220 ]
2.0.0 Ready to start TLS

Error:
(535, '5.7.8 Error: authentication failed: authentication failure')
```

詳しくは[こちら](https://nitchmo.com/check-smtp-auth.html)
