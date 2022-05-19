# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Custom
    Key([mod], "p", lazy.spawn("rofi -show run")),
    Key([], "Print", lazy.spawn("flameshot gui")),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
     layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = {
    "background": '#181818',
    "current_line": '#282828',
    "foreground": '#f8f8f2',
    "comment": '#535453',
    "black":   '#181818',
    "red":     '#ab4642',
    "green":   '#a1b56c',
    "yellow":  '#f7ca88',
    "blue":    '#7cafc2',
    "magenta": '#ba8baf',
    "cyan":    '#86c1b9',
    "white":   '#d8d8d8',
}

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.Sep(
                       linewidth=0,
                       padding=5,
                       foreground=colors['background'],
                       background=colors['background']
                ),
                widget.TextBox(
                    text="",
                    padding=5,
                    fontsize=30,
                    foreground=colors['red'],
                    background=colors['background']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                
                widget.GroupBox(
                font='JetBrainsMono Bold',
                    fontsize=12,
                highlight_method='block',
                background=colors['background'],
                this_current_screen_border='f7ca88',
                active='#FFFFFF',
                inactive='#FFFFFF',
                    
                ),
               # widget.Prompt(),
                widget.TextBox(
                    text='\uE0B0',
                    background=colors['current_line'],
                    foreground=colors['background'],
                    padding=0,
                    fontsize=25
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['current_line'],
                    background=colors['current_line']
                ),
                widget.WindowName(
                    padding=5,
                    background=colors['current_line'],
                    foreground=colors['foreground'],
                    empty_group_string="Desktop",
                    max_chars=130,
                ),
                # widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # widget.Systray(),
               # widget.Clock(format="%d-%m-%Y %a %I:%M %p"),
               widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='',
                    background=colors['yellow'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=15
                ),
               widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='MEMORY:',
                    background=colors['yellow'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=10
                ),
                widget.Memory(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['background'],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        "alacritty" + ' -e htop')},
                    fmt='{}',
                    padding=5,
                    background=colors['white']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='',
                    background=colors['blue'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=15
                ),
               widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='CPU:',
                    background=colors['blue'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=10
                ),
                widget.CPU(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['background'],
                    background=colors['white'],
                    format='{load_percent}%',
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='',
                    background=colors['magenta'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=15
                ),
                widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='CLOCK:',
                    background=colors['magenta'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=10
                ),
                widget.Clock(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['background'],
                    background=colors['white'],
                    format="%B %d %a %I:%M %p",
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='',
                    background=colors['red'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=15
                ),
                widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='SYS:',
                    background=colors['red'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=10
                ),
                widget.Systray(
                foreground=colors['background'],
                background=colors['white'],
                padding=5
                ),
                # widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
