import nox


@nox.session(python=["3.12", "3.13"], venv_backend="uv")
def tests(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--group",
        "dev",
        "--frozen",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("pytest", *session.posargs)
