from .doodles import doodle_bp

def init_app(app):
    app.register_blueprint(doodle_bp)