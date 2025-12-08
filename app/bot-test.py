import discord, random
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
TOKEN = ""

TIER_DICT = {
    "브론즈": "b",
    "실버": "s",
    "골드": "g",
    "플래티넘": "p",
    "다이아": "d",
    "루비": "r",
}

TIER_CHOICE = [app_commands.Choice(name=name, value=value) for name, value in TIER_DICT.items()]
DIFFICULTY_CHOICE = [app_commands.Choice(name=str(value), value=str(value)) for value in range(1, 6)]

# ----------------------
# 임시 문제 데이터
# ----------------------
problems = {
    1: {"title": "Two Sum", "difficulty": "Easy"},
    2: {"title": "Binary Tree Paths", "difficulty": "Medium"},
    3: {"title": "Dijkstra Path", "difficulty": "Hard"},
}

# ----------------------
# 문제 선택 버튼 View
# ----------------------
class ProblemListView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        for pid, pdata in problems.items():
            self.add_item(ProblemButton(label=pdata["title"], problem_id=pid))


class ProblemButton(discord.ui.Button):
    def __init__(self, label, problem_id):
        super().__init__(style=discord.ButtonStyle.primary, label=label)
        self.problem_id = problem_id

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"**{problems[self.problem_id]['title']}** 문제 선택됨.\n수정할 내용을 입력해주세요!",
            view=EditProblemView(self.problem_id),
            ephemeral=True
        )

# ----------------------
# 문제 수정 View (확인 버튼 포함)
# ----------------------
class EditProblemView(discord.ui.View):
    def __init__(self, problem_id):
        super().__init__(timeout=None)
        self.problem_id = problem_id

        # 임시 저장 공간
        self.selected_name = None
        self.selected_number = None

        # Select 추가
        self.add_item(DifficultyNameSelect(self))
        self.add_item(DifficultyNumberSelect(self))

        # 확인 버튼 추가
        self.add_item(ConfirmDifficultyButton(self))


# ----------------------
# 난이도 이름(단계) Select
# ----------------------
class DifficultyNameSelect(discord.ui.Select):
    def __init__(self, parent_view):
        self.parent_view = parent_view

        options = [
            discord.SelectOption(label="Easy", value="Easy"),
            discord.SelectOption(label="Medium", value="Medium"),
            discord.SelectOption(label="Hard", value="Hard"),
        ]

        super().__init__(
            placeholder="난이도 단계 선택",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        self.parent_view.selected_name = self.values[0]
        await interaction.response.defer(ephemeral=True)


# ----------------------
# 난이도 숫자 Select
# ----------------------
class DifficultyNumberSelect(discord.ui.Select):
    def __init__(self, parent_view):
        self.parent_view = parent_view

        options = [
            discord.SelectOption(label=str(i), value=str(i))
            for i in range(1, 6)
        ]

        super().__init__(
            placeholder="난이도 숫자 선택 (1~5)",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        self.parent_view.selected_number = self.values[0]
        await interaction.response.defer(ephemeral=True)


# ----------------------
# 확인 버튼
# ----------------------
class ConfirmDifficultyButton(discord.ui.Button):
    def __init__(self, parent_view):
        super().__init__(label="확인", style=discord.ButtonStyle.success)
        self.parent_view = parent_view

    async def callback(self, interaction: discord.Interaction):
        name = self.parent_view.selected_name
        number = self.parent_view.selected_number

        # 둘 다 선택 완료해야만 적용
        if name is None or number is None:
            return await interaction.response.send_message(
                "⚠ 난이도 단계와 숫자를 모두 선택해주세요.",
                ephemeral=True
            )

        # 최종 난이도 저장
        pid = self.parent_view.problem_id
        problems[pid]["difficulty"] = f"{name} {number}"

        await interaction.response.send_message(
            f"✅ 최종 난이도 업데이트 완료!\n"
            f"문제: **{problems[pid]['title']}**\n"
            f"새 난이도: **{name} {number}**",
            ephemeral=True
        )

# 로그인
@bot.event
async def on_ready():
    print(f"{bot.user.name} 로그인 성공")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)}")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping", description="test")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("aaa")


@bot.tree.command(name="daily_setting", description="문제를 구조화해서 등록합니다.")
@app_commands.describe(
    min_tier="최소 티어",
    min_difficulty="최소 난이도",
    max_tier="최대 티어",
    max_difficulty = "최대 난이도",
    no_dup = "푼 사람이 없는 문제만"
)
@app_commands.choices(
    min_tier=TIER_CHOICE,
    min_difficulty=DIFFICULTY_CHOICE,
    max_tier=TIER_CHOICE,
    max_difficulty=DIFFICULTY_CHOICE,
    no_dup=[
        app_commands.Choice(name="yes", value=1),
        app_commands.Choice(name="no", value=0),
    ]
)
async def register(
    interaction: discord.Interaction,
    min_tier: app_commands.Choice[str],
    min_difficulty: app_commands.Choice[str],
    max_tier: app_commands.Choice[str],
    max_difficulty: app_commands.Choice[str],
    no_dup: app_commands.Choice[int]
):
    await interaction.response.send_message(
        f"""📌 **수정 완료!**
        **최소 난이도:** {min_tier.name}{min_difficulty.name}
        **최대 난이도:** {max_tier.name}{max_difficulty.name}
        **푼 사람이 없는 문제만:** {no_dup.name}
        """
    )


@bot.tree.command(name="pong", description="test")
async def pong(interaction: discord.Interaction):
    await interaction.response.send_message("aaa")


@bot.tree.command(name="prob_list", description="문제 리스트를 출력합니다")
async def prob_list(
        interaction: discord.Interaction
):
    embed = discord.Embed(title="문제 목록", color=0x00AACC)
    for pid, p in problems.items():
        embed.add_field(
            name=f"{pid}. {p['title']}",
            value=f"난이도: {p['difficulty']}",
            inline=False,
        )

    await interaction.response.send_message(
        embed=embed,
        view=ProblemListView()
    )

# 봇 작동
bot.run(TOKEN)