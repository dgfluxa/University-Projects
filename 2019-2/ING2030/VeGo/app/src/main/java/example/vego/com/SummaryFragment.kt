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
class SummaryFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view: View = inflater.inflate(R.layout.fragment_summary, container, false)

        var nutri_list = view.findViewById<ListView>(R.id.nutri_list)
        var list = mutableListOf<Nutrition>()

        list.add(Nutrition("Proteinas", "53"))
        list.add(Nutrition("Hierro", "34"))
        list.add(Nutrition("Vitamina B12", "30"))
        list.add(Nutrition("Vitamina A", "67"))
        list.add(Nutrition("Vitamina C", "80"))
        list.add(Nutrition("Calcio", "76"))
        list.add(Nutrition("Calorías", "90"))
        list.add(Nutrition("Potasio", "80"))

        nutri_list.adapter = NutriAdapter(activity!!.applicationContext, R.layout.nutri_row, list)

        nutri_list.setOnItemClickListener { parent: AdapterView<*>, view:View, position:Int, id:Long ->
            Toast.makeText( activity!!.applicationContext, "Información no disponible", Toast.LENGTH_LONG).show()

        }


        return view
    }


}
