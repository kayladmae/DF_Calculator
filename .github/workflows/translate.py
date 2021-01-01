#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, re, glob

Translations = {    
    ##These are fucked. Need someone who speaks Korean to translate for me.
    '크리티컬 확률은 장비 세팅의 유연성에 ': 'Critical probability depends on the flexibility of equipment setting',
    '영향을 미칩니다. 직업마다 보정되는 크': 'The size is corrected for each job',
    '리티컬 확률이 다르고 투자한 수준에 ': 'Rittal odds are different and the level of investment',
    '따라 커버할 수 있는 수치도 다릅니다. ': 'The numbers that can be covered are different for each',
    '만크를 채울 수 있는지를 체크하는 것이 ': 'Checking whether it can be filled',
    '중요합니다.': 'important',
    '속도 옵션은 게임 플레이의 쾌적성에 ': 'Checking whether mank can be filled',
    '큰 영향을 미칩니다. 데미지에 직접적 ': 'Checking whether mank can be filled',
    '영향을 주지는 않지만, 게임의 재미에 ': 'It doesn\'t affect the game, but the fun of the game',
    '직결되므로 낮은 속도는 추천하지 않습': 'I do not recommend a low speed because it is directly connected',
    '니다. 다만 직업과 플레이어 기호에 ': 'Just profession and player preference',
    '따라 요구치가 다르므로 스스로 점검해': 'Just the profession and player preference',
    '보는 것이 좋습니다.': 'Good to see',
    
    "지연/랜덤 데미지 옵션은 스킬 빌드에 큰": "Delayed/random damage options are great for skill build",
    "영향을 줍니다. 지나친 지연딜은 방 클리": "It has an impact. Excessive delay is a bang-klee",
    "어에 부정적인 효과를 주며, 지나친 랜덤": "Negative effect. Excessive randomness",
    "딜은 일관된 스킬 빌드 정립을 방해합니다.": "The deal interferes with the establishment of a consistent skill build.",
    "적당한 패널티 옵션은 게임에 활력을 주": "The right penalty option gives the game a boost",
    "지만, 과하면 딜링에 부정적인 영향을 줍": 'However, if it is excessive, it will negatively affect your dealings',
    "니다. 패널티의 작용은 유저의 실력, 딜링": "No. Penalty is the user's ability and dealings",
    "환경, 직업에 따라 다르므로 스스로 점검": 'It depends on the environment and job, so check yourself',
    "해보는 것이 좋습니다.": 'Good to try',
    '높은 각성 레벨링, 각성기 스증 등 상대적': 'High arousal leveling, awakening spirit, etc. relative',
    '으로 그로기에서 우세한 스킬 특화의 데미': 'Demi of skill specialization that is dominant in grogi',
    '지 옵션이 많습니다. 그로기 비중이 높다': 'There are a lot of paper options. There is a lot of growth.',
    '면 장점으로 안정적인 딜링을 가지지만, ': 'I have a stable dealing as an advantage of noodles,',
    '지속딜에 비해 낮은 데미지 포텐셜을 보여': 'Shows lower damage potential compared to sustained deals',
    '준다는 단점이 있습니다.': 'There is a downside to giving.',
    '특히 직업에 따라 각성기 계수가 낮거나 ': 'Especially, depending on the job, the awakening factor is low',
    '좋은 지속딜 스킬셋을 보유중인 직업이라': 'It\'s a job that has a good lasting deal skill set',
    '면, 그로기 위주의 세팅을 하지 않는 것이 ': 'If you don\'t set up mainly for growth,',
    '좋습니다.': 'good.',
    '여담으로 던파오프 또한 그로기 세팅의 우위만 보여주므로, ': 'As an aside, Dunpa-off also only shows the superiority of the grogi setting,',
    '검증시 주의하는 것이 좋습니다.': 'It is good to be careful when verifying.',


    '쿨타임 감소율은 높은 지속딜 포텐셜과 ': 'Cooldown reduction is a high sustained deal potential',
    '호쾌한 게임 플레이를 가능케하지만, 지나': 'Allows exciting gameplay, but Gina',
    '치게 높은 쿨타임 감소율은 스킬의 타점과 ': 'The extremely high cooldown reduction rate is the RBI of the skill',
    '범위, 채널링에 따라 그 스킬의 제 성능을 ': 'According to the range, channeling, the best performance of that skill',
    '내지 못하게 만들 수 있습니다. 또 그로기': 'You can make it impossible to do it. And Groggy',
    '라는 안정적 딜링 환경과 달리 지속딜은 ': 'Unlike the stable dealing environment of , sustainable deals are',
    '움직이는 적을 상대로 하기 때문에 파일럿': 'Pilot because you are against moving enemies',
    '의 역량 또한 매우 중요합니다. ': 'The competence of is also very important.',
    '본인의 직업이 평타기/각성기 비중이 높고 ': '“My job has a high percentage of pacifying/awakening”',
    '스킬 사이클을 빠르게 돌릴 수 없거나, ': 'You can\'t run the skill cycle fast,',
    '지속딜에 자신이 없다면 과한 쿨타임 감소 ': 'If you are not confident in the ongoing deal, excessive cooldown decreases',
    '세팅은 피하는 것이 좋습니다.': 'It is better to avoid the setting.',


    '흐름셋은 단일 스킬레벨 구간에 매우 높은 ': 'Flow set is very high in a single skill level section',
    '쿨감과 동시에 데미지 감소를 적용시킵니다. ': 'Damage reduction is applied at the same time as the cool feeling.',
    '이론상 해당 스킬의 데미지 증가율은 40%': 'Theoretically, the damage increase rate of this skill is 40%',
    '지만, 쿨이 올 때마다 쓰지 못한다면 효율': 'But, if you can\'t use it every time cool comes, efficiency',
    '이 떨어집니다. 또 흐름셋 매커니즘이 특수': 'The flow set mechanism is special.',
    '하게 적용되는 직업도 많아 반드시 자기 직': 'There are a lot of jobs that apply to each other, so be sure to do your job',
    '업 기준의 정보를 수집해야 합니다.\n\n': 'You need to gather up-level information.\n\n',
    '탈리스만 선택 신발은 캐릭의 탈리스만 ': 'Talisman\'s shoes are only Carrick\'s Talisman',
    '스킬 비중에 따라 효율이 달라집니다. 흐름': 'Efficiency varies depending on the proportion of the skill. Flow',
    '과 마찬가지로 쿨감 효율을 제대로 받을 수 ': 'Like you can get cool feeling efficiency properly',
    '있는지도 체크해봐야 합니다. 계산기 상 탈': 'You have to check if it exists. Get on the calculator',
    '리스만 선택의 효율은 실제 평균보다 살짝 ': 'The efficiency of the Lismann selection is slightly less than the actual average',
    '높게 잡혀있습니다.': 'It is held high.',

    '그 직업의 특정 스킬 공격력 증가(또는 쿨감), 피깎, 쿨초 등 ': 'Increase (or cool) the attack power of a certain skill of that job, blood cut, cool second, etc.',
    '데미지에 직접적인 영향을 미치는 특수한 옵션을 보유하고 있습니다. ': '“We have special options that directly affect the damage.”',
    '그 옵션이 무엇인지, 그리고 사용 직업이 그 옵션을 제대로 살릴 수 있는지, ': 'What are the options, and whether the job you are using can make use of those options,',
    '또 플레이어의 기호에 그 옵션이 맞는지 점검해보는 것이 좋습니다.\n': 'Also, it\'s a good idea to check that the option fits your preferences.\n',
    '하지만 이 모든 것을 떠나 세팅에 있어서 긍정적인 효과를 가진 것은 확실합니다.': '“But apart from all this, it certainly has a positive effect on the setting.”',

    '슈퍼아머, 파티 버프 등 딜링 환경을 조성하는데 있어 긍정적인 효과를 보유하고 있습니다. ': 'It has a positive effect in creating a dealing environment such as Super Armor and Party Buff.',
    '대게 이런 효과를 가진 장비는 대부분 데미지 값이 낮게 설계되어 있지만, ': 'Most equipment with this effect is designed with a low damage value',
    '개인 또는 파티 전체에 높은 안정성을 제공해주므로 데미지 수치에 비해 ': 'Compared to the damage level because it provides high stability to individuals or the entire party',
    '높은 파티 선호도를 가진 것 또한 사실입니다.': 'It\'s also true that they have a high party preference.',

    '세팅의 그로기-지속딜 데미지 차이 수준을 나타냅니다. ': 'Indicates the level of the difference between the setting\'s grogi and sustained damage.',
    '파란색은 지속딜이 그로기에 비해 n% 우위임을 뜻하고, ': 'Blue means lasting deals have an n% advantage over Groggy,',
    '빨간색은 그로기가 지속딜에 비해 n% 우위임을 뜻합니다. ': '"Red means Grogg has an n% advantage over sustained deals."',
    '계산기 설정에서 쿨감 보정값과 그로기의 쿨감 보정 유무, ': 'In the calculator setting, the cool feeling correction value and the presence or absence of the cool feeling correction of the Grogi,',
    '그리고 해당 직업의 무기별 쿨감에 영향을 받습니다. ': 'And it is affected by the coolness of each weapon for that job.',
    '특히 쿨감과 쿨증 무기를 둘 모두 쓰는 직업은 계산 기준이 되는 무기를 잘 체크해야 합니다. ': 'Especially for jobs that use both cool and cool weapons, you need to check the weapon that is the basis of calculation.',

    '\n\n검신/검제: 광검  /  닼나: 소검\n로그: 쌍검\n스커: 권글\n엘마/소환사: 스태프': '\n\nSword/Sword: Light Sword / Tonna: Short Sword\nLog: Double Sword\nSkirt: Kwon\nElma/Summoner: Staff',

    '최종 데미지%의 정의는 \'동일 직업 노마부 마봉 캐릭보다 얼마나 더 강한지\' 입니다. ': 'The definition of the final damage% is how much stronger than Mabong Carrick, the Norman of the same job.',
    '따라서 각 세팅 별 데미지 차이율은 두 데미지% 값을 나누면 됩니다.\n': 'So, the damage difference rate for each setting can be divided by the two damage% values.\n',
    '자속강 보유 직업의 경우 속성강화 옵션의 효율이 떨어지고, 노마부 마봉 기준 데미지가 타직업에 비해 높아 ': 'In the case of a job with magnetic flux, the efficiency of the attribute enhancement option is low, and the damage based on the no-mabu mabong is higher than that of other jobs.',
    '데미지%가 낮게 나오는 것이 정상입니다. ': 'It is normal for the damage% to come out low.',
    '다만 타직업과 장비 수준을 비교하고 싶다는 요청이 많아 하단에 자속강이 없는 기준의 %도 추가했습니다.': 'However, there are many requests to compare the level of equipment with other occupations, so we have also added a percentage of the standard without flux steel at the bottom.',

    ##These ones are much better
    '단품제외': 'Exclude single item',
    '미충족': 'Unmet',
    
    '에러': 'Error',
    'API 접근 권한 획득 실패': 'Failed to obtain API access',
    '패치노트': 'Patch Notes',
    '업데이트': 'Update',
    '업데이트 텍스트 파일 누락': 'Missing update text file',
    '업데이트 실패. 엑셀을 닫고 다시 실행해주세요': 'Close Excel and run again',
    '클라이언트 버전': 'Client version',
    '엑셀 버전': 'Excel version',
    
    
    '귀검사(남)': 'Slayer(M)',
    '검신(진각)': 'Blade Master',
    '다크로드(진각)': 'Soul Bender',
    '블러드이블(진각)': 'Berserker',
    '인다라천(진각)': 'Asura',
    '악귀나찰(진각)': 'Ghostblade',

    '귀검사(여)': 'Slayer(F)',
    '마제스티(진각)': 'Sword Master',
    '디어사이드(진각)': 'Demon Slayer',
    '네메시스(진각)': 'Nemesis',
    '검제(진각)': 'Vagabond',

    '격투가(남)': 'Fighter(M)',
    '염황광풍제월(진각)': 'Nen Master',
    '패황(진각)': 'Striker',
    '명왕(진각)': 'Brawler',
    '그랜드마스터(진각)': 'Grappler',

    '격투가(여)': 'Fighter(F)',
    '염제폐월수화(진각)': 'Nen Master',
    '카이저(진각)': 'Striker',
    '용독문주(진각)': 'Brawler',
    '얼티밋디바(진각)': 'Grappler',

    '거너(남)': 'Gunner(M)',
    '레이븐(진각)': 'Ranger',
    '디스트로이어(진각)': 'Launcher',
    '프라임(진각)': 'Mechanic',
    '커맨더(진각)': 'Spitfire',

    '거너(여)': 'Gunner(F)',
    '크림슨로제(2각)': 'Ranger',
    '스톰트루퍼(2각)': 'Launcher',
    '옵티머스(2각)': 'Mechanic',
    '프레이야(2각)': 'Spitfire',

    '마법사(남)': 'Mage(M)',
    '오블리비언(진각)': 'Elemental Bomber',
    '이터널(진각)': 'Glacial Master',
    '뱀파이어로드(진각)': 'Blood Mage',
    '아이올로스(진각)': 'Swfit Master',
    '어센션(진각)': 'Dimension Walker',

    '마법사(여)': 'Mage(F)',
    '오버마인드(진각)': 'Elementalist',
    '이클립스(진각)': 'Summoner',
    '아슈타르테(진각)': 'Battle Mage',
    '지니위즈(진각)': 'Witch',
    '(버프)헤카테(진각)': 'Enchantress',

    '프리스트(남)': 'Priest(M)',
    '세인트(진각)': 'Crusader (Battle)',
    '(버프)세인트(진각)': 'Crusader (Buff)',
    '저스티스(진각)': 'Monk',
    '태을선인(진각)': 'Exorcist',
    '이모탈(진각)': 'Avenger',

    '프리스트(여)': 'Priest(F)',
    '(버프)세라핌(진각)': 'Crusader',
    '인페르노(진각)': 'Inquisitor',
    '천선낭랑(진각)': 'Shaman',
    '리디머(진각)': 'Mistress',

    '도적': 'Thief',
    '알키오네(진각)': 'Rogue',
    '타나토스(진각)': 'Necromancer',
    '시라누이(진각)': 'Kunoichi',
    '그림리퍼(진각)': 'Shadow Dancer',

    '나이트': 'Knight',
    '가이아(2각)': 'Elven Knight',
    '마신(2각)': 'Chaos',
    '세이비어(2각)': 'Lightbringer',
    '드레드노트(2각)': 'Dragon Knight',

    '마창사': 'Demonic Lancer',
    '듀란달(2각)': 'Skirmisher',
    '워로드(2각)': 'Vanguard',
    '제노사이더(2각)': 'Dragoon',
    '에레보스(2각)': 'Impaler',

    '총검사': 'Agent',
    '갓파더(2각)': 'Hitman',
    '레퀴엠(2각)': 'Secret Agent',
    '언터처블(2각)': 'Trouble Shooter',
    '패스파인더(2각)': 'Specialist',

    '외전': 'Supplemental',
    '다크나이트(2각)': 'Dark Knight',
    '크리에이터(2각)': 'Creator',

    '버퍼': 'Buffer',
    '(버프)세인트(진각)': 'Saint',
    '(버프)세라핌(진각)': 'Seraph',
    '(버프)헤카테(진각)': 'Hekate',
    
    '眞인챈트리스': 'Enchantress',
    
    '진각': 'Advanced',
    '2각': '2nd Awakening',
    '무기': 'Weapon',
    '귀걸이': 'Earring',
    '상의': 'Top',
    '팔찌': 'Bracelet',
    '칭호': 'Title',
    '목걸이': 'Necklace',
    '반지': 'Ring',
    '마법석': 'Magic Stone',
    '하의': 'Bottom',
    '보조장비': 'Special Equipment',
    '화속성강화': 'Fire',
    '수속성강화': 'Water',
    '명속성강화': 'Light',
    '암속성강화': 'Darkness',
    '모든 속성 강화': 'All Elemental',
    '물리 공격력': 'PAtk',
    '마법 공격력': 'MAtk',
    '독립 공격력': 'IAtk',
    
    '소검': 'Short Sword',
    '둔기': 'Bludgeon',
    '대검': 'Zanbato',
    '쌍검': 'Double Sword', ##wat
    '단검': 'Daggers',
    '광검': 'Lightsabre',
    '도': 'Katana',
    
    '플래티넘': 'Platinum',
    '레전더리': 'Legendary',
    '언커먼': 'Uncommon',
    '공통': 'Common',
    '갈라진': 'Split',
    '온전한': 'Intact',
}

os.chdir('..')
directory = glob.glob('*.py')

for word in Translations:
    for file in directory:
        open_file = open(file,'r')
        read_file = open_file.read()
        regex = re.compile(word)
        if len(re.findall(regex, read_file)) > 0:
            read_file = regex.sub(Translations[word], read_file)
            write_file = open(file,'w')
            write_file.write(read_file)
            print('replaced '+word+' with '+Translations[word])
