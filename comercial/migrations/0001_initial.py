# Generated by Django 4.0.4 on 2022-07-10 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dep_pessoal', '0003_remove_falta_cid_atestado_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteOrcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_client', models.CharField(max_length=80, verbose_name='CLIENTE')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dep_pessoal.funcionario', verbose_name='CONSULTOR')),
            ],
            options={
                'verbose_name': 'CLIENTE / ORÇAMENTO',
                'verbose_name_plural': 'CLIENTE / ORÇAMENTOS',
            },
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.IntegerField(verbose_name='ORÇAMENTO Nº')),
                ('term_survey', models.BooleanField(default=False, verbose_name='TERMO DE VISTORIA')),
                ('sketch', models.BooleanField(default=False, verbose_name='CROQUI')),
                ('survey', models.BooleanField(default=False, verbose_name='VISTORIA')),
                ('alter_budget', models.BooleanField(default=False, verbose_name='ALTERAÇÃO ORÇAMENTO')),
                ('budget_closure', models.BooleanField(default=False, verbose_name='FECHAMENTO DO ORÇAMENTO')),
                ('send_dp_accept', models.BooleanField(default=False, verbose_name='ENVIO DP ACEITE')),
                ('acceptance_confirmation', models.BooleanField(default=False, verbose_name='CONFIRMAÇÃO DE ACEITE')),
                ('antecipation', models.BooleanField(default=False, verbose_name='ANTECIPAÇÃO')),
                ('confirmation_payment', models.BooleanField(default=False, verbose_name='CONFIRMAÇÃO DE PAGAMENTO')),
                ('releaser_installation', models.BooleanField(default=False, verbose_name='LIBERADO PARA INSTALAÇÃO')),
                ('request_reopening', models.BooleanField(default=False, verbose_name='SOLICITAÇÃO PARA REABERTURA DE O.S')),
                ('obs', models.TextField(max_length=1000, verbose_name='OBSERVAÇÃO')),
                ('client_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comercial.clienteorcamento', verbose_name='CLIENTE')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dep_pessoal.funcionario', verbose_name='CONSULTOR')),
            ],
            options={
                'verbose_name': 'ORÇAMENTO',
                'verbose_name_plural': 'ORÇAMENTOS',
            },
        ),
        migrations.CreateModel(
            name='Vistoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AGENDADO', 'AGENDADO'), ('NÃO INICIADO', 'NÃO INICIADO'), ('INICIADO', 'INICIADO'), ('PAUSADO', 'PAUSADO'), ('FINALIZADO', 'FINALIZADO'), ('ENTREGUE', 'ENTREGUE')], default='NÃO INICIADO', max_length=15, verbose_name='STATUS')),
                ('date_start', models.DateField(blank=True, verbose_name='Data Inicio')),
                ('date_fin', models.DateField(blank=True, null=True, verbose_name='Data Fim')),
                ('date_delivery', models.DateField(blank=True, null=True, verbose_name='Data Entrega')),
                ('alteration', models.BooleanField(verbose_name='COM ALTERAÇÃO')),
                ('no_alteration', models.BooleanField(default=True, verbose_name='SEM ALTERAÇÃO')),
                ('obs_eqp_alter', models.TextField(blank=True, max_length=1000, verbose_name='OBSERVAÇÃO DE EQUIPAMENTOS')),
                ('obs_implant_alter', models.TextField(blank=True, max_length=1000, verbose_name='OBSERVAÇÃO DE IMPLANTAÇÃO')),
                ('obs_service_alter', models.TextField(blank=True, max_length=1000, verbose_name='OBSERVAÇÃO DE SERVIÇO')),
                ('obs_infra_alter', models.TextField(blank=True, max_length=1000, verbose_name='OBSERVAÇÃO DE INFRAESTRUTURA')),
                ('budget_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ORÇAMENTO', to='comercial.orcamento', verbose_name='ORÇAMENTO Nº')),
                ('client_survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CLIENTE / ORÇAMENTO+', to='comercial.clienteorcamento', verbose_name='CLIENTE')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CONSULTOR', to='dep_pessoal.funcionario', verbose_name='CONSULTOR')),
            ],
            options={
                'verbose_name': 'VISTORIA',
                'verbose_name_plural': 'VISTORIAS',
            },
        ),
    ]
