import boto3


def cognito_auth(username, email, gender, birthday, nickname):
    # 認証開始
    try:
        aws_client = boto3.client('cognito-idp',
            region_name = 'ap-northeast-1',
            aws_access_key_id = '***',
            aws_secret_access_key = '***',
        )

        # ユーザー作成
        aws_result = aws_client.admin_create_user(
            # cognito設定時のユーザープールID
            UserPoolId='***',
            Username=username,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'gender',
                    'Value': gender
                },
                {
                    'Name': 'birthdate',
                    'Value': birthdate
                },
                {
                    'Name': 'nickname',
                    'Value': nickname
                },
            ],
            # Mailに初期パスワードを送信する
            DesiredDeliveryMediums=['EMAIL']
        )

        # 認証完了
        print(aws_result)

    except:
        # 認証失敗
        print('Error')


cognito_auth('username', 'email', 'gender', 'birthdate', 'nickname')