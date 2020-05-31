
class Experiment:
    masa = []
    tau = []
    viteza = []

    def __init__(self, viteza=None, tau=None, masa=None, raza_discului=None, masa_discului = None):

        if viteza is not None:
            self.viteza.append(viteza)
        if tau is not None:
            self.tau.append(tau)
        if masa is not None:
            self.masa.append(masa)
        if raza_discului is not None:
            self.raza_discului = raza_discului
        if masa_discului is not None:
            self.masa_discului = masa_discului

    def lastTry(self, viteza0, tau0):
        self.viteza0 = viteza0
        self.tau0 = tau0

    def normalF(self):
        self.Normal = [mas*9.8 for mas in self.masa]
        return self.Normal

    def frictionF(self):
        self.J = (self.masa_discului*self.raza_discului**2)/2
        self.Friction = [((self.J*self.viteza0)/(self.raza_discului*self.tau0)) * ((self.tau0/tau)-1) for tau in self.tau]
        return self.Friction, self.J

    def coef(self, Normal, Friction):
        return [f/n for f, n in zip(Friction, Normal)]

    @property
    def Momentul_rezistentei(self):
        return (self.J * self.viteza0) / self.tau0

    def error(self):
        delta_r = 0.005
        delta_tau = delta_tau0 = 0.5
        delta_w = 0.5
        delta_m = 0.005
        m_av = sum(self.masa) / len(self.masa)
        w_av = sum(self.viteza) / len(self.viteza)
        tau_av = sum(self.tau) / len(self.tau)
        f_av = sum(self.Friction) / len(self.Friction)

        eps_f = (2*((delta_m/m_av) + (2*delta_r/self.raza_discului))) + (2*delta_w/w_av) + (2*delta_tau0/self.tau0) + (2*delta_tau/tau_av) + (2*delta_r/self.raza_discului)
        delta_f = eps_f * f_av
        return eps_f, delta_f

    def restart(self):
        self.masa.clear()
        self.viteza.clear()
        self.tau.clear()
        self.Normal.clear()
        self.Friction.clear()
        del self.raza_discului
        del self.masa_discului
        del self.J


# (viteza , tau, masa)
Model1 = Experiment(100, 2, 9, 0.25, 3)
Experiment(100, 2.3, 8)
Experiment(100, 2.6, 7)
Experiment(100, 3.1, 6)
Experiment(100, 3.7, 5)
Experiment(100, 4.5, 4)
Experiment(100, 6, 3)
Experiment(100, 8.8, 2)
Experiment(100, 16.5, 1)
Model1.lastTry(100, 120)


NormalForce = Model1.normalF()
FrictionForce, J = Model1.frictionF()
Coefs = Model1.coef(NormalForce, FrictionForce)
print('...First Model...')
print('Normal force list: ', *['%.3f'% elem for elem in NormalForce], sep=' |')
print('Fricion force list:', *['%.3f'% elem for elem in FrictionForce], sep=' |')
print('Coefs list:        ', *['%.3f'% elem for elem in Coefs], sep=' |')
print('')
MomentulRezistentei = Model1.Momentul_rezistentei
print('Momentul de inertie:', J)
print('Momentul rezistentei:', MomentulRezistentei)

Eps_friction, Delta_friction = Model1.error()
print('Epsilon Friction: {:.3}%'.format(Eps_friction))
print('Delata Friction: {:.3}'.format(Delta_friction))
print('...End First Model...\n')
Model1.restart()


Model2 = Experiment(1000, 18, 9, 0.25, 3)
Experiment(1000, 19, 8)
Experiment(1000, 22, 7)
Experiment(1000, 25, 6)
Experiment(1000, 29, 5)
Experiment(1000, 34, 4)
Experiment(1000, 41, 3)
Experiment(1000, 53, 2)
Experiment(1000, 73, 1)
Model2.lastTry(100, 120)

NormalForce = Model2.normalF()
FrictionForce, J = Model2.frictionF()
Coefs = Model2.coef(NormalForce, FrictionForce)
print('...Second Model...')
print('Normal force list: ', *['%.3f'% elem for elem in NormalForce], sep=' |')
print('Fricion force list:', *['%.3f'% elem for elem in FrictionForce], sep=' |')
print('Coefs list:        ', *['%.3f'% elem for elem in Coefs], sep=' |')
print('')
MomentulRezistentei = Model2.Momentul_rezistentei
print('Momentul de inertie:', J)
print('Momentul rezistentei:', MomentulRezistentei)

Eps_friction, Delta_friction = Model2.error()
print('Epsilon Friction: {:.3}%'.format(Eps_friction))
print('Delata Friction: {:.3}'.format(Delta_friction))
print('...End Second Model...')