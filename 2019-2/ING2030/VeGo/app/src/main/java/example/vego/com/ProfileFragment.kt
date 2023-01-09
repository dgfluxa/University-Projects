package example.vego.com


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ListView
import android.widget.Toast

/**
 * A simple [Fragment] subclass.
 */
class ProfileFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view: View = inflater.inflate(R.layout.fragment_profile, container, false)

        var profile_list = view.findViewById<ListView>(R.id.profile_list)
        var list = mutableListOf<Setting>()

        list.add(Setting("Editar Perfil"))
        list.add(Setting("Recetas Favoritas"))
        list.add(Setting("Personalizar Alimentación"))
        list.add(Setting("Detección de Actividad Física"))
        list.add(Setting("Opciones de App"))



        profile_list.adapter = SetAdapter(activity!!.applicationContext, R.layout.profile_row, list)

        profile_list.setOnItemClickListener { parent: AdapterView<*>, view:View, position:Int, id:Long ->

                Toast.makeText( activity!!.applicationContext, "No accesible", Toast.LENGTH_LONG).show()

        }


        return view
    }


}
