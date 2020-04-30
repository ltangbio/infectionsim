"""
Module for particles which simulate people in an infection simulation.
"""
import random


class Particle:
    """
    An actor in a simulation of infection spread.

    Attributes
    ----------
    x : float
        x coordinate of the particle.
    y : float
        y coordinate of the particle.
    vx : float
        x velocity of the particle.
    vy : float
        y velocity of the particle.
    is_infected : bool
        Tracks whether the actor is infected.
    infection_timer : float, optional
        Time until the actor is no longer infected (either recovers or dies).
    is_alive : bool
        Determines whether the actor is alive (default is True).
    has_recovered : bool
        Determines whether an uninfected actor has already had the infection
        and recovered from it (default is False).
    transmission_prob : float
        Probability that actor will transmit the infection to another actor in
        a collision if the actor is infected.
    infection_prob : float
        Probability that the actor will be infected by a tramissive collion with
        another actor if the actor is not infecte.
    survival_prob : float
        Probability that the actor will recover after the infection_timer runs
        out.
    """

    def __init__(self, x, y, vx, vy, is_infected, infection_timer, transmission_prob, infection_prob, survival_prob):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
        self._is_infected = is_infected
        self._infection_timer = infection_timer
        self._is_alive = True
        self._has_recovered = False
        self._transmission_prob = transmission_prob
        self._infection_prob = infection_prob
        self._survival_prob = survival_prob

    def __repr__(self):
        """
        String representation of a particle.
        """
        return "<InfectionSim Particle at: x={:.2f}, y={:.2f}>".format(self._x, self._y)

    @property
    def x(self):
        """
        Getter for x coordinate of a particle.

        Returns
        -------
        float
            The x coordinate of a particle.
        """
        return self._x

    @property
    def y(self):
        """
        Getter for the y coordinate of a particle.

        Returns
        -------
        float
            The y coordinate of a particle.
        """
        return self._y

    @property
    def is_alive(self):
        """
        Getter for the is_alive status of a particle.

        Returns
        -------
        bool
            Whether or not the particle is alive.
        """
        return self._is_alive

    def update_position(self, dt):
        """
        Update the position of the particle by one timestep.

        Parameters
        ----------
        dt : float
            The size of the timestep.

        Notes
        -----
        Currently in simple form which does not take into account collisions or
        the bounding box. Remove this note once these features are added.
        Features for timer and recovery/death also need to be implemented.
        """
        self._x += self._vx * dt
        self._y += self._vy * dt

        # TODO: Add timer countdown if infected and logic for dying/recovering.

    def update_velocity_collision(self, other):
        """
        Update the velocity of the particle when a collision happens.

        Parameters
        ----------
        other : Particle
            The other particle that `self` is colliding with.

        Raises
        ------
        NoteImplementedError
            Because the functionality has not been implemented.

        Notes
        -----
        Needs to consider angle of impact and then compute conservation of
        momentum between the particles for a perfectly elastic collision.
        """
        raise NotImplementedError

    def decide_infect(self, other):
        """
        Decide whether infection is spread during a collision between two
        particles, using the various probability parameters.

        Parameters
        ----------
        other : Particle
            The other particle that `self` is colliding with.
        """
        if (self._is_infected and not other._is_infected):
            if random.random() < self._transmission_prob and random.random() < other._infection_prob:
                other._is_infected = True

        if other._is_infected and not self._is_infected:
            if random.random() < other._transmission_prob and random.random() < self._infection_prob:
                self._is_infected = True
