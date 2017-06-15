<tr class="noCover">
<td class="line"><a name='1'/>1</td>
<td class="hits"/>
<td class="code">#/usr/bin/env&nbsp;python</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='2'/>2</td>
<td class="hits">1</td>
<td class="code">"""This&nbsp;module&nbsp;provides&nbsp;functions&nbsp;for&nbsp;authenticating&nbsp;users."""</td>
</tr>
<tr class="noCover">
<td class="line"><a name='3'/>3</td>
<td class="hits"/>
<td class="code"></td>
</tr>
<tr class="coverFull">
<td class="line"><a name='4'/>4</td>
<td class="hits">1</td>
<td class="code">def&nbsp;login(username,&nbsp;password):</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='5'/>5</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;try:</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='6'/>6</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_file&nbsp;=&nbsp;open('/etc/users.txt')</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='7'/>7</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_buf&nbsp;=&nbsp;user_file.read()</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='8'/>8</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users&nbsp;=&nbsp;[line.split("|")&nbsp;for&nbsp;line&nbsp;in&nbsp;user_buf.split("\n")]</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='9'/>9</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;[username,&nbsp;password]&nbsp;in&nbsp;users:</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='10'/>10</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;True</td>
</tr>
<tr class="noCover">
<td class="line"><a name='11'/>11</td>
<td class="hits"/>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='12'/>12</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;False</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='13'/>13</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;except&nbsp;Exception,&nbsp;exc:&nbsp;#TODO&nbsp;-&nbsp;To&nbsp;remove&nbsp;the&nbsp;unused&nbsp;variable.</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='14'/>14</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print&nbsp;"I&nbsp;can't&nbsp;authenticate&nbsp;you."</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='15'/>15</td>
<td class="hits">1</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;False</td>
</tr>
<tr class="noCover">
<td class="line"><a name='16'/>16</td>
<td class="hits"/>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
</tr>
<tr class="coverFull">
<td class="line"><a name='17'/>17</td>
<td class="hits">1</td>
<td class="code">def&nbsp;logout():</td>
</tr>
<tr class="coverNone">
<td class="line"><a name='18'/>18</td>
<td class="hits">0</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;print&nbsp;'this&nbsp;line&nbsp;will&nbsp;not&nbsp;be&nbsp;covered&nbsp;by&nbsp;test&nbsp;cases.'</td>
</tr>
<tr class="coverNone">
<td class="line"><a name='19'/>19</td>
<td class="hits">0</td>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;print&nbsp;'this&nbsp;line&nbsp;will&nbsp;not&nbsp;be&nbsp;covered&nbsp;by&nbsp;test&nbsp;cases&nbsp;as&nbsp;well.'</td>
</tr>
<tr class="noCover">
<td class="line"><a name='20'/>20</td>
<td class="hits"/>
<td class="code">&nbsp;&nbsp;&nbsp;&nbsp;</td>
</tr>
<tr class="noCover">
<td class="line"><a name='21'/>21</td>
<td class="hits"/>
<td class="code">#URGENT&nbsp;-&nbsp;signup()&nbsp;function&nbsp;to&nbsp;add&nbsp;ASAP.</td>
</tr>
