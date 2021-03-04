/* jshint esversion: 6 */
require('dotenv').config();

const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');
const port= process.env.PORT || 3000;

const app = express();

///////////////////SETTINGS////////////////
app.set('view engine','ejs');
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended:true}));


mongoose.connect("mongodb+srv://"+process.env.USER_DB+":"+process.env.PASS_DB+"@proyectoprogramacion.u4hsj.mongodb.net/ProyectoProgramacion?retryWrites=true&w=majority", {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const pacienteSchema= new mongoose.Schema({
    nombres: String,
    apellidos: String,
    email: String,
    password: String,
    celular: Number,
    edad: Number,
    direccion: String,
    centro: String,
    departamento: String,
    ciudad: String,
    dni:Number,
    cat:String


});

const Paciente = mongoose.model('Paciente',pacienteSchema);

const medicoSchema= new mongoose.Schema({
    nombres: String,
    apellidos: String,
    email: String,
    password: String,
    celular: Number,
    edad: Number,
    colegiatura:Number,
    especialidad:String,
    direccion: String,
    centro: String,
    departamento: String,
    ciudad: String,
    dni:Number,
    cat:String


});

const Medico = mongoose.model('Medico',medicoSchema);





//////////////////ROUTES////////////////////////
app.get('/', (req,res)=>{
    res.render('index');
});


app.get('/kit_medico', (req,res)=>{
    res.render('kit_medico');
    
});
app.get('/conocenos', (req,res)=>{
    res.render('conocenos');
    
});

app.get('/desc_gui_paciente', (req,res)=>{
    res.render('desc_gui_paciente');
    
});
app.get('/desc_gui_medico', (req,res)=>{
    res.render('desc_gui_medico');
    
});
app.get('/reg_paciente', (req,res)=>{
    res.render('reg_paciente');
    
});
app.get('/reg_medico', (req,res)=>{
    res.render('reg_medico');
    
});

app.post('/reg_paciente', (req, res)=>{
    
    const nuevoPaciente = new Paciente({
        nombres: req.body.nombres_pa,
        apellidos: req.body.apellidos_pa,
        email: req.body.email_pa,
        password: req.body.password_pa,
        celular: req.body.celular_pa,
        edad: req.body.edad_pa,
        direccion: req.body.direccion_pa,
        centro: req.body.centro_pa,
        departamento: req.body.departamento_pa,
        ciudad: req.body.ciudad_pa,
        dni:req.body.dni_pa,
        cat:"paciente"


    });
    nuevoPaciente.save();
    
    res.redirect('/');
    
});





app.post('/reg_medico', (req, res)=>{
    const nuevoMedico = new Medico({
        nombres: req.body.nombres_med,
        apellidos: req.body.apellidos_med,
        email: req.body.email_med,
        password: req.body.password_med,
        celular: req.body.celular_med,
        edad: req.body.edad_med,
        colegiatura: req.body.colegiatura,
        especialidad: req.body.especialidad,
        direccion: req.body.direccion_med,
        centro: req.body.centro_med,
        departamento: req.body.departamento_med,
        ciudad: req.body.ciudad_med,
        dni:req.body.dni_med,
        cat:"medico"


    });
    nuevoMedico.save();
    
    res.redirect('/');
    
});











///////////////SERVIDOR///////////////////////////
app.listen(port, () => {
    console.log(`Servidor  en puerto ${port}`);
});