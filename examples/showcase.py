import time

from awe import Page


def main():
    now = time.time()
    page = Page('Showcase')
    grid = page.new_grid(columns=3, props={'gutter': 12})
    grid.new_card('Card 1')
    card = grid.new_card()
    tabs = grid.new_tabs()
    collapse = grid.new_collapse()
    grid.new_chart([(now+i, -i) for i in range(100)], transform='numbers')
    grid.new_table(['Header 1', 'Header 2', 'Header 3'], page_size=4).extend([
        ['Value {}'.format(i), 'Value {}'.format(i+1), 'Value {}'.format(i+2)]
        for i in range(1, 20, 3)
    ])
    grid.new_divider()
    grid.new_button(lambda: None, 'Button 1', block=True)
    grid.new_input()
    grid.new_icon('heart', theme='twoTone', two_tone_color='red')
    inline = grid.new_inline()
    card.new_text('Card Text 1')
    card.new_text('Card Text 2')
    tabs.new_tab('Tab 1').new_link('https://github.com/dankilman/awe').new_text('Tab 1 Link')
    tabs.new_tab('Tab 2').new_text('Tab 2 Text')
    tabs.new_tab('Tab 3').new_text('Tab 3 Text')
    tabs.new_tab('Tab 4').new_text('Tab 4 Text')
    collapse.new_panel('Panel 1', active=True).new_text('Panel 1 Text')
    collapse.new_panel('Panel 2').new_text('Panel 2 Text')
    collapse.new_panel('Panel 3').new_text('Panel 3 Text')
    collapse.new_panel('Panel 4').new_text('Panel 4 Text')
    collapse.new_panel('Panel 5').new_text('Panel 5 Text')
    inline.new_inline('inline 1')
    inline.new_inline('inline 2')
    inline.new_inline('inline 3')
    page.start(block=True)


if __name__ == '__main__':
    main()
