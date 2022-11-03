<p>Incremental game</p>
<p><br></p>
<p>The game will be a Wine production game, where the player will manage a winery.</p>
<p><br></p>
<p>There are 3 field of action:</p>
<p><br></p>
<p>-Vineyards</p>
<p>-Winery</p>
<p>-Sales/Marketing</p>
<p><br></p>
<p>The player can perform different activities</p>
<p><br></p>
<p>Vineyards:</p>
<p>- increment vineyards level</p>
<p>- Harvest ( every N hours)</p>
<p><br></p>
<p>Winery</p>
<p>- increase winery level</p>
<p>- Produce wine ( every N hours)</p>
<p><br></p>
<p>Sales/Marketing</p>
<p>- increase Marketing level</p>
<p>- collect money from sales</p>
<p><br></p>
<p><br></p>
<p>As with all incremental games, the player&apos;s goal is to increase the amount of money earned.</p>
<p>The player gets this money based on the number of bottles he can sell. The player can spend the money to raise the level of each of the three fields of action in order to increase their hourly production (grapes, bottles, money).</p>
<p><br></p>
<p>Bot Commands</p>
<p><br></p>
<p>The games are run via bots. The game is capable of executing management-related commands via chat commands. The commands are divided into categories depending on whether they are system commands, customization commands or action commands.</p>
<p><br></p>
<h1>System commands</h1>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Command</p>
                </td>
                <td>
                    <p>Effect</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!help&nbsp;</p>
                </td>
                <td>
                    <p>Opens the command summary and help panel</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!startwinery&nbsp;</p>
                </td>
                <td>
                    <p>Create a new Winery</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!deletewinery [winery_name]</p>
                </td>
                <td>
                    <p>Delete a Winery (Must be case sensitive)</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!changeGrapeVariety [new]</p>
                </td>
                <td>
                    <p>Change the grape</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p>Winery will have a name and a grape variety the player can choose from a list</p>
<p><br></p>
<h1>Customization commands</h1>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Command</p>
                </td>
                <td>
                    <p>Effect</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!newName</p>
                </td>
                <td>
                    <p>change winery name</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!stats&nbsp;</p>
                </td>
                <td>
                    <p>show the 3 field of action level, status and overall money&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!levelupWinery</p>
                </td>
                <td>
                    <p>level up Winery (Can&rsquo;t be used if Bottling is ongoing)evel up</p>
                    <p>54</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - production increase</p>
                    <p>55</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - Activity T</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!levelupVineyards</p>
                </td>
                <td>
                    <p>level up Vineyards (Can&rsquo;t be used if Harvest is ongoing)</p><br>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!levelupMarketing</p>
                </td>
                <td>
                    <p>level up Marketing (Can&rsquo;t be used if Selling is ongoing)</p><br>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!nextLevelInfo</p>
                </td>
                <td>
                    <p>show info of the next level of Winery, vineyards, marketing such as:<br>- cost to level up<br>- production increase</p>
                    <p>- Activity Time</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!nextOperation</p>
                </td>
                <td>
                    <p>shows next operation required of user</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<h1>Action commands</h1>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Command</p>
                </td>
                <td>
                    <p>Effect</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!harvest&nbsp;</p>
                </td>
                <td>
                    <p>Start the grape harvesting</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!harvestInfo&nbsp;</p>
                </td>
                <td>
                    <p>Shows how much time is left before harvesting is done</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!harvestEnd&nbsp;</p>
                </td>
                <td>
                    <p>Collect the Harvest result</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!winemaking&nbsp;</p>
                </td>
                <td>
                    <p>Start wine production</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!winemakinginfo&nbsp;</p>
                </td>
                <td>
                    <p>Show how much time is left before the winemaking is done</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!bottling</p>
                </td>
                <td>
                    <p>Collect the wine bottles</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!selling&nbsp;</p>
                </td>
                <td>
                    <p>Start selling</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>!sellinginfo&nbsp;</p>
                </td>
                <td>
                    <p>Show how much time is left before the selling is done</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<h1>Field of action Data</h1>
<p><br></p>
<p>Vineyard</p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Data</p>
                </td>
                <td>
                    <p>Description</p>
                </td>
                <td>
                    <p>Value</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Level</p>
                </td>
                <td>
                    <p>The level of the Vineyards</p>
                </td>
                <td>
                    <p>Int</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>LevelUp Cost</p>
                </td>
                <td>
                    <p>The price to increase the level of Vineyards</p>
                </td>
                <td>
                    <p>Int</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Vineyard Production Bonus&nbsp;</p>
                </td>
                <td>
                    <p>The bonus of production given to the harvest (at this level)</p>
                </td>
                <td>
                    <p>Float</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Harvest Time</p>
                </td>
                <td>
                    <p>The time need to complete the Harvest Task (at this level)</p>
                </td>
                <td>
                    <p>Time</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p>Winery</p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Data</p>
                </td>
                <td>
                    <p>Description</p>
                </td>
                <td>
                    <p>Value</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Level</p>
                </td>
                <td>
                    <p>The level of the Winery</p>
                </td>
                <td>
                    <p>Int</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>LevelUp Cost</p>
                </td>
                <td>
                    <p>The price to increase the level of Winery</p>
                </td>
                <td>
                    <p>Int</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Winery Production Bonus</p>
                </td>
                <td>
                    <p>The bonus of production given to the bottling (at this level)</p>
                </td>
                <td>
                    <p>Float</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Bottling Time</p>
                </td>
                <td>
                    <p>The time need to complete the Bottling Task</p>
                </td>
                <td>
                    <p>Time</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p>Marketing/Warehouse</p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Data</p>
                </td>
                <td>
                    <p>Description</p>
                </td>
                <td>
                    <p>Value</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Level</p>
                </td>
                <td>
                    <p>The level of Marketing/Warehouse</p>
                </td>
                <td>
                    <p>Int</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>LevelUp Cost</p>
                </td>
                <td>
                    <p>The price to increase the level of Marketing/Warehouse</p>
                </td>
                <td>
                    <p>Int</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Price Bonus</p>
                </td>
                <td>
                    <p>The bonus of price&nbsp;</p>
                </td>
                <td>
                    <p>Float</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Selling Time</p>
                </td>
                <td>
                    <p>The time to complete the Selling task</p>
                </td>
                <td>
                    <p>Time</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<h1><br><br>How the game works<br><br><br>The end goal is to produce as much money as possible.</h1>
<p><br></p>
<h2>Harvest Formula</h2>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Base Production * Vineyard Production Bonus =&nbsp;</p>
                    <p>Grape production</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<h2>Bottling Formula</h2>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Grape production *0,75 * Winery Production Bonus =&nbsp;</p>
                    <p>Bottles production</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<h2>Selling Formula</h2>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>(Bottles production * Base Price * price bonus)/&nbsp;Selling Time=&nbsp;</p>
                    <p>Money x Sec</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<p>Vineyard</p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>BASE PRODUCTION = 9000</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p>&nbsp;</p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Level</p>
                </td>
                <td>
                    <p>LevelUp Cost</p>
                </td>
                <td>
                    <p>Vineyard Production Bonus</p>
                </td>
                <td>
                    <p>Time</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>7000</p>
                </td>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>12 hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>14000</p>
                </td>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>10 hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>150000</p>
                </td>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>8 hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>4</p>
                </td>
                <td>
                    <p>1000000</p>
                </td>
                <td>
                    <p>4</p>
                </td>
                <td>
                    <p>6 hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>-</p>
                </td>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>4 hours</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p>Winery</p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Level</p>
                </td>
                <td>
                    <p>LevelUp Cost</p>
                </td>
                <td>
                    <p>Winery Production Bonus</p>
                </td>
                <td>
                    <p>Time</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>7000</p>
                </td>
                <td>
                    <p>0.5</p>
                </td>
                <td>
                    <p>6 Hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>14000</p>
                </td>
                <td>
                    <p>0.55</p>
                </td>
                <td>
                    <p>5 Hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>150000</p>
                </td>
                <td>
                    <p>0.6</p>
                </td>
                <td>
                    <p>4 Hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>4</p>
                </td>
                <td>
                    <p>1000000</p>
                </td>
                <td>
                    <p>0.7</p>
                </td>
                <td>
                    <p>3 Hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>-</p>
                </td>
                <td>
                    <p>0.75</p>
                </td>
                <td>
                    <p>2 Hours</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p>Marketing</p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>BASE PRICE = 7</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Level</p>
                </td>
                <td>
                    <p>LevelUp Cost</p>
                </td>
                <td>
                    <p>Price Bonus</p>
                </td>
                <td>
                    <p>Time (sec)</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>7000</p>
                </td>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>4 Hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>14000</p>
                </td>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>3 Hours 30 min</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>150000</p>
                </td>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>3 Hours</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>4</p>
                </td>
                <td>
                    <p>1000000</p>
                </td>
                <td>
                    <p>4</p>
                </td>
                <td>
                    <p>2 Hours 30 minu</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>-</p>
                </td>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>2 Hours</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br>Leaderboard wipe<br>The leaderboard will be wiped every 2 weeks. Before the wipe take place the bot post the leaderboard and then it will wipe the following player data:<br>- Money<br>- Field of action levels<br>- Reset ongoing operations<br><br>The best things would be to include a countdown in the leaderboard to the next wipe<br>&nbsp;<img src="https://lh6.googleusercontent.com/VOux3Yn6sYWmqhwoPhHGbp8OsU1_sE0vxunOZ61HyHfsdPzxfaUfjj4qcKdfNfumMvxKko2bNyJBZrpXdt5L0-1EvUiRMScTMqh4IpIYp3i33iUrdUuzD8Z8QeV2NrNyb8-BwIeSGqAxCaNpcmou1mLhczfJuxUAN5MW7fuUqDxyxtbVLr8PIpmA3MQ" width="419" height="321"><br><br><br><br><br>Grape List<br>Barbera</p>
<p>Chardonnay</p>
<p>Nebbiolo</p>
<p>Arneis</p>
<p>Dolcetto</p>
<p>Cortese</p>
<p>Grignolino</p>
<p>Cabernet S.</p>
<p>Sauvignon B.</p>
<p>Zinfandel</p>
<p>Riesling</p>
<p>Pinot noir</p>
<p>Merlot</p>
<p>Syrah</p>
<p><br></p>
<p><br></p>
<p><br></p>
<p>Game Rule and Description<br>The Discord wine game is a Wine production game, where the player will manage a winery.</p>
<p><br></p>
<p>There are 3 field of action:</p>
<p><br></p>
<h1>🍇Vineyards</h1>
<h1>🍇Winery</h1>
<h1>🍇Sales/Marketing</h1>
<p><br></p>
<p>You can perform different activities:</p>
<p><br></p>
<p>Vineyards:</p>
<h1>🍇&nbsp;increment vineyards level</h1>
<h1>🍇&nbsp;Harvest ( every N hours)</h1>
<p><br></p>
<p>Winery</p>
<h1>🍇increase winery level</h1>
<h1>🍇&nbsp;Produce wine ( every N hours)</h1>
<p><br></p>
<p>Sales/Marketing</p>
<h1>🍇&nbsp;increase Marketing level</h1>
<h1>🍇&nbsp;collect money from sales</h1>
<p><br></p>
<p><br></p>
<p>As with all incremental games, your goal is to increase the amount of money earned.</p>
<p>Every Two weeks the leaderboard will be reset</p>
<p><br></p>
<p><br></p>
<p><br></p>
