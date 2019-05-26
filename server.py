#!/usr/bin/python3

import flask

import hp
import whale


if __name__ == "__main__":
    def main():
        app = flask.Flask(__name__)
        hp_server = hp.Server()
        whale_game = hp.Game("whale", whale.Room)
        assert hp_server.add_game(app, whale_game)

        #
        # Assets:
        #

        @app.route("/")
        def index():
            return flask.render_template("index.html")

        @app.route("/whale")
        def whale_page():
            game_id = whale_game.id
            room_id = whale_game.add_room()
            player_id = whale_game.add_player(room_id)
            return flask.render_template("whale.html", game_id=game_id, room_id=room_id, player_id=player_id)

        @app.route("/js/<path:sub_path>")
        def js(sub_path):
            return flask.send_from_directory("js/", sub_path)

        @app.route("/css/<path:sub_path>")
        def css(sub_path):
            return flask.send_from_directory("css/", sub_path)

        @app.route("/img/<res>/<path:name>")
        def img(res, name):
            if res == "svg":
                return flask.send_from_directory("img/svg", f"{name}.svg")
            elif res == "x1":
                return flask.send_from_directory("img/x1", f"{name}.png")
            elif res == "x2":
                return flask.send_from_directory("img/x2", f"{name}.png")
            else:
                # Default to 3x resolution for unknown 'res' strings:
                return flask.send_from_directory("img/x3", f"{name}.png")

        @app.route("/font/<path:sub_path>")
        def font(sub_path):
            return flask.send_from_directory("font", sub_path)

        @app.route("/audio/<path:sub_path>")
        def audio(sub_path):
            return flask.send_from_directory("audio/", sub_path)

        #
        # Game (can be moved to a different server for load-balancing!
        #

        # app.run(debug=False, host="0.0.0.0")
        app.run()

    main()


# TODO:
#  - Fix hover-on and hover-off triggers. You can't track grid positions, you need to track active tiles.

# TODO:
#  - Animation:
#    - Hover colors for choices
#    - Click animation (feedback)
#    - Page transitions
#  - Tracking a user:
#    - Server/DB integration
#    - Cookies
#    - Score persistence (account system)
#  - Gameplay:
#    - Two more levels

# Fixes:
#  - Got 'hover_on' and 'hover_off' working.

# Tickets:
#  - Hosting 'getwhaled' for info or correcting the URL the button currently points at.

# TODO: (minor)
#  - Set fixed font sizes for font objects
#  - Add mouse-over functionality, change buttons' colors.
#  - Add suffices to denote whether position values are in grid, dip (device independent pixel), or pix form.
