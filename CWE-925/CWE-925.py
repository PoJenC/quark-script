from quark.script import isCheckMethodsCalledInTarget, getReceivers

SAMPLE_PATH = "AndroGoat.apk"

TARGET_METHOD = [
    '',
    'onReceive',
    '(Landroid/content/Context; Landroid/content/Intent;)V'
]

CHECK_METHODS = [
    ['Landroid/content/Intent;', 'getAction', '()Ljava/lang/String;']
]

receivers = getReceivers(SAMPLE_PATH)
for receiver in receivers:
    if receiver.isExported():
        className = "L"+str(receiver).replace('.', '/')+';'
        TARGET_METHOD[0] = className
        if not isCheckMethodsCalledInTarget(SAMPLE_PATH, TARGET_METHOD, CHECK_METHODS):
            print(f"CWE-925 is detected in method, {className}")
