from .hurtfulwords import hurtfulwords


def setup(bot):
    bot.add_cog(hurtfulwords())
